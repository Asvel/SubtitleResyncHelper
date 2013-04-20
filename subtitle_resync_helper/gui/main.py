# -*- coding: utf-8 -*-

import os
from collections import OrderedDict, namedtuple

import pysubs
from PyQt4.QtCore import Qt, pyqtSignal
from PyQt4.QtGui import (QMainWindow, QFileDialog, QMessageBox,
                         QTreeWidgetItem, QTreeWidget)

from subtitle_resync_helper import config, timemap, shifter
from subtitle_resync_helper.gui.timemaper import FormTimeMapper
from subtitle_resync_helper.gui.main_ui import Ui_MainWindow


class FormMain(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(FormMain, self).__init__()

        def _get_filename(self):
            return os.path.join(self.text(1), self.text(0))
        def _set_filename(self, filename):
            head, tail = os.path.split(filename)
            self.setText(0, tail)
            self.setText(1, head)
        QTreeWidgetItem.filename = property(_get_filename, _set_filename)
        def _children(self):
            for i in range(self.childCount()):
                yield self.child(i)
        QTreeWidgetItem.children = _children

        self.setupUi(self)

        self.ct_trees = [
            ('src', self.ct_tree_src),
            ('dst', self.ct_tree_dst),
        ]

        for qtree in self.ct_trees:
            qtree[1].hideColumn(1)

        self.ct_start.setShortcut(config.shortcut['main_start'])

    def __new_qtreewidgetitem(self, filename):
        qitem = QTreeWidgetItem()
        qitem.filename = filename
        return qitem

    def qtreewidegt_getitems(self, qtreewidget):
        items = OrderedDict()
        for i in range(qtreewidget.topLevelItemCount()):
            qitem = qtreewidget.topLevelItem(i)
            items[qitem.filename] = {x.filename for x in qitem.children()}
        return items

    def qtreewidegt_setitems(self, qtreewidget, items):
        qtreewidget.clear()
        for parent in items:
            children = sorted(items[parent])
            qitem = self.__new_qtreewidgetitem(parent)
            for child in children:
                qitem.addChild(self.__new_qtreewidgetitem(child))
            qtreewidget.addTopLevelItem(qitem)

    def appenditems_src(self, qtree):
        # 扩展名筛选
        fileext_video = config.fileext_video
        fileext_subtitle = config.fileext_subtitle
        filter_video = " ".join(["*." + x for x in fileext_video])
        filter_subtitle = " ".join(["*." + x for x in fileext_subtitle])
        filter_video_sub = " ".join([filter_video, filter_subtitle])
        filedialog_filter = "视频与字幕 ({});;视频 ({});;字幕 ({})".format(
            filter_video_sub, filter_video, filter_subtitle)

        # 获取文件列表
        filelist = QFileDialog.getOpenFileNames(self, "选择原始文件",
            config.filedialog_lastdir, filedialog_filter)
        if len(filelist) > 0:
            config.filedialog_lastdir = os.path.dirname(filelist[0])
        filelist = [x for x in filelist if os.path.isfile(x)]

        # 显示文件列表
        filelist_subtitle = []
        for i in reversed(range(len(filelist))):
            if os.path.splitext(filelist[i])[1][1:] in fileext_subtitle:
                filelist_subtitle.insert(0, filelist.pop(i))
        items = self.qtreewidegt_getitems(qtree)
        for filename in filelist:
            if filename not in items:
                items[filename] = set()
        for subtitle in filelist_subtitle:
            for video in items:
                if subtitle.startswith(os.path.splitext(video)[0]):
                    items[video].add(subtitle)
                    break
        self.qtreewidegt_setitems(qtree, items)
        qtree.resizeColumnToContents(0)

    def appenditems_dst(self, qtree):
        # 扩展名筛选
        fileext_video = config.fileext_video
        filter_video = " ".join(["*." + x for x in fileext_video])
        filedialog_filter = "视频 ({})".format(filter_video)

        # 获取文件列表
        filelist = QFileDialog.getOpenFileNames(self, "选择目标文件",
            config.filedialog_lastdir, filedialog_filter)
        if len(filelist) > 0:
            config.filedialog_lastdir = os.path.dirname(filelist[0])
        filelist = [x for x in filelist if os.path.isfile(x)]

        # 显示文件列表
        items = self.qtreewidegt_getitems(qtree)
        for filename in filelist:
            if filename not in items:
                items[filename] = set()
        self.qtreewidegt_setitems(qtree, items)
        qtree.resizeColumnToContents(0)

    def removeitems(self, qtree):
        for item in qtree.selectedItems():
            parent = item.parent()
            if parent is None:
                parent = qtree.invisibleRootItem()
            parent.removeChild(item)

    def clearitems(self, qtree):
        qtree.clear()

    def cleanitems_src(self, qtree):
        for i in reversed(range(qtree.topLevelItemCount())):
            qitem = qtree.topLevelItem(i)
            if qitem.childCount() == 0:
                qtree.takeTopLevelItem(i)

    def cleanitems_dst(self, qtree):
        video_counts = [x[1].topLevelItemCount() for x in self.ct_trees
                        if x[0] == 'src']
        video_count = min(video_counts)
        if video_count == max(video_counts):
            for i in reversed(range(video_count, qtree.topLevelItemCount())):
                qtree.takeTopLevelItem(i)
        else:
            QMessageBox.error(self, "错误", "目标文件列表中视频数不同")

    def start_resync(self):
        # 文件列表
        types, trees = zip(*self.ct_trees)
        if min([x.topLevelItemCount() for x in trees]) < 1:
            QMessageBox.error(self, "错误", "文件列表中没有文件")
        videos = [x.topLevelItem(0).filename for x in trees]

        # 获取时间映射表
        try:
            self.hide()
            timemapper = FormTimeMapper(types, videos)
            timemapper.exec()
            print(timemapper.timemap)
        finally:
            self.show()
            self.setFocus()

        # 准备文件名
        videos_src = []
        videos_dst = []
        timelists_src = []
        timelists_dst = []
        subtitless_src = []
        for type, tree, video, timelist in \
            zip(types, trees, videos, timemapper.timemap):
            if type == 'src':
                videos_src.append(video)
                timelists_src.append(timelist)
                subtitless_src.append([x.filename for x in
                                       tree.topLevelItem(0).children()])
            else:
                videos_dst.append(video)
                timelists_dst.append(timelist)
            tree.takeTopLevelItem(0)

        for video_dst, timelist_dst in zip(videos_dst, timelists_dst):
            for video_src, timelist_src, subtitles_src in \
                zip(videos_src, timelists_src, subtitless_src):
                timedelta = timemap.normalize(zip(timelist_src, timelist_dst))
                for sub_src in subtitles_src:
                    # 生成字幕文件名
                    video_src_mainname = os.path.splitext(
                        os.path.split(video_src)[1])[0]
                    sub_src_name = os.path.split(sub_src)[1]
                    video_dst_mainname = os.path.splitext(
                        os.path.split(video_dst)[1])[0]
                    if sub_src_name.startswith(video_src_mainname):
                        sub_dst_name = video_dst_mainname + \
                                       sub_src_name[len(video_src_mainname):]
                    else:
                        sub_dst_name = sub_src_name
                    sub_dst = os.path.join(os.path.dirname(video_dst),
                                           sub_dst_name)

                    # 调整字幕
                    subs = pysubs.load(sub_src)
                    shifter.shift(subs, timedelta)
                    subs.info['Resync Info'] = str(timedelta)
                    subs.save(sub_dst)

    def ct_tree_itemexpanded(self, item):
        self.sender().resizeColumnToContents(0)

    def ct_tree_itemcollapsed(self, item):
        self.sender().resizeColumnToContents(0)

    def ct_append_src_clicked(self):
        qtree = self.sender().parent().findChild(QTreeWidget)
        self.appenditems_src(qtree)

    def ct_append_dst_clicked(self):
        qtree = self.sender().parent().findChild(QTreeWidget)
        self.appenditems_dst(qtree)

    def ct_remove_clicked(self):
        qtree = self.sender().parent().findChild(QTreeWidget)
        self.removeitems(qtree)

    def ct_clear_clicked(self):
        qtree = self.sender().parent().findChild(QTreeWidget)
        self.clearitems(qtree)

    def ct_clean_src_clicked(self):
        qtree = self.sender().parent().findChild(QTreeWidget)
        self.cleanitems_src(qtree)

    def ct_clean_dst_clicked(self):
        qtree = self.sender().parent().findChild(QTreeWidget)
        self.cleanitems_dst(qtree)

    def ct_start_clicked(self):
        self.start_resync()
