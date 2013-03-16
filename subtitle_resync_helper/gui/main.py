# -*- coding: utf-8 -*-

import os
from collections import OrderedDict

from PyQt4.QtCore import Qt, pyqtSignal
from PyQt4.QtGui import QMainWindow, QFileDialog, QTreeWidgetItem, QMessageBox

from subtitle_resync_helper import config
from subtitle_resync_helper.gui.timemaper import FormTimeMapper
from subtitle_resync_helper.gui.main_ui import Ui_MainWindow


class FormMain(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(FormMain, self).__init__()
        self.setupUi(self)

        self.ct_trees = [
            {'type':'src', 'obj':self.ct_tree_src},
            {'type':'dst', 'obj':self.ct_tree_dst},
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

        items, order = self.qtreewidegt_getitems(qtree)
        for filename in filelist:
            if filename not in items:
                items[filename] = set()
                order.append(filename)
        self.qtreewidegt_setitems(qtree, items, order)
        qtree.resizeColumnToContents(0)

    def start_resync(self):
        video_counts = [x['obj'].topLevelItemCount()-1 for x in self.ct_trees]
        video_count = min(video_counts)
        if video_count != max(video_counts):
            QMessageBox.warning(self, "警告", "列表中视频数不同")

        for i in range(video_count):
            qitems = [x['obj'].topLevelItem(i) for x in self.ct_trees]
            files = [x.text(0) for x in qitems]
            timemapper = FormTimeMapper([{'type':q['type'], 'path':p}
                for q, p in zip(self.ct_trees, files)])
            timemapper.exec()
            print(timemapper.timemap)

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
