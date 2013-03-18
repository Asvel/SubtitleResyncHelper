# -*- coding: utf-8 -*-

import os
from collections import OrderedDict, namedtuple

import pysubs
from PyQt4.QtCore import Qt, pyqtSignal
from PyQt4.QtGui import QMainWindow, QFileDialog, QTreeWidgetItem, QMessageBox

from subtitle_resync_helper import config, timemap, shifter
from subtitle_resync_helper.gui.timemaper import FormTimeMapper
from subtitle_resync_helper.gui.main_ui import Ui_MainWindow


class FormMain(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(FormMain, self).__init__()
        self.setupUi(self)

        self.ct_trees = [
            ('src', self.ct_tree_src),
            ('dst', self.ct_tree_dst),
        ]

    def qtreewidegt_getitems(self, qtreewidget):
        items = OrderedDict()
        for i in range(qtreewidget.topLevelItemCount() - 1):
            qitem = qtreewidget.topLevelItem(i)
            items[qitem.text(0)] = {qitem.child(i).text(0)
                                   for i in range(qitem.childCount())}
        return items

    def qtreewidegt_setitems(self, qtreewidget, items):
        for i in reversed(range(qtreewidget.topLevelItemCount() - 1)):
            qtreewidget.takeTopLevelItem(i)
        for parent in items:
            children = sorted(items[parent])
            qitem = QTreeWidgetItem([parent])
            for child in children:
                qitem.addChild(QTreeWidgetItem([child]))
            qtreewidget.insertTopLevelItem(
                qtreewidget.topLevelItemCount() - 1, qitem)

    def addfiles_src(self, qtree):
        fileext_video = config.fileext_video
        fileext_subtitle = config.fileext_subtitle

        filter_video = " ".join(["*." + x for x in fileext_video])
        filter_subtitle = " ".join(["*." + x for x in fileext_subtitle])
        filter_video_sub = " ".join([filter_video, filter_subtitle])
        filedialog_filter = "视频与字幕 ({});;视频 ({});;字幕 ({})".format(
            filter_video_sub, filter_video, filter_subtitle)
        filelist = QFileDialog.getOpenFileNames(self, "选择原始文件",
            config.filedialog_lastdir, filedialog_filter)
        if len(filelist) > 0:
            config.filedialog_lastdir = os.path.dirname(filelist[0])

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

    def addfiles_dst(self, qtree):
        fileext_video = config.fileext_video

        filter_video = " ".join(["*." + x for x in fileext_video])
        filedialog_filter = "视频 ({})".format(filter_video)
        filelist = QFileDialog.getOpenFileNames(self, "选择目标文件",
            config.filedialog_lastdir, filedialog_filter)
        if len(filelist) > 0:
            config.filedialog_lastdir = os.path.dirname(filelist[0])

        items = self.qtreewidegt_getitems(qtree)
        for filename in filelist:
            if filename not in items:
                items[filename] = set()
        self.qtreewidegt_setitems(qtree, items)
        qtree.resizeColumnToContents(0)

    def start_resync(self):
        types, trees = zip(*self.ct_trees)
        trees = [self.qtreewidegt_getitems(x) for x in trees]
        video_counts = [len(x) for x in trees]
        video_count = min(video_counts)
        if video_count != max(video_counts):
            QMessageBox.warning(self, "警告", "列表中视频数不同")

        for videos in zip(*trees):
            timemapper = FormTimeMapper(types, videos)
            timemapper.exec()
            print(timemapper.timemap)

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
                    subtitless_src.append(tree[video])
                else: # type == 'dst'
                    videos_dst.append(video)
                    timelists_dst.append(timelist)

            for video_dst, timelist_dst in zip(videos_dst, timelists_dst):
                for video_src, timelist_src, subtitles_src in \
                    zip(videos_src, timelists_src, subtitless_src):
                    timedelta = timemap.normalize(
                        zip(timelist_src, timelist_dst))
                    for sub_src in subtitles_src:
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

                        subs = pysubs.load(sub_src)
                        shifter.shift(subs, timedelta)
                        subs.save(sub_dst)


    def ct_start_clicked(self):
        self.start_resync()

    def ct_tree_src_clicked(self, item, column):
        qtree = self.sender()
        if qtree.indexOfTopLevelItem(item) + 1 == qtree.topLevelItemCount():
            self.addfiles_src(qtree)

    def ct_tree_dst_clicked(self, item, column):
        qtree = self.sender()
        if qtree.indexOfTopLevelItem(item) + 1 == qtree.topLevelItemCount():
            self.addfiles_dst(qtree)

    def ct_tree_itemexpanded(self, item):
        self.sender().resizeColumnToContents(0)

    def ct_tree_itemcollapsed(self, item):
        self.sender().resizeColumnToContents(0)
