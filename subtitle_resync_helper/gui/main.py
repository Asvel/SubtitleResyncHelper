# -*- coding: utf-8 -*-

import os

from PyQt4.QtCore import Qt, pyqtSignal
from PyQt4.QtGui import QMainWindow, QKeySequence, QFileDialog, QTreeWidgetItem

from subtitle_resync_helper import config, player, time
from subtitle_resync_helper.gui.main_ui import Ui_MainWindow


class FormMain(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(FormMain, self).__init__()
        self.setupUi(self)

    def qtreewidegt_getitems(self, qtreewidget):
        items = {}
        order = []
        for i in range(qtreewidget.topLevelItemCount() - 1):
            qitem = qtreewidget.topLevelItem(i)
            items[qitem.text(0)] = {qitem.child(i).text(0)
                                   for i in range(qitem.childCount())}
            order.append(qitem.text(0))
        return items, order

    def qtreewidegt_setitems(self, qtreewidget, items, order):
        for i in reversed(range(qtreewidget.topLevelItemCount() - 1)):
            qtreewidget.takeTopLevelItem(i)
        for parent in order:
            children = sorted(items[parent])
            qitem = QTreeWidgetItem([parent])
            for child in children:
                qitem.addChild(QTreeWidgetItem([child]))
            qtreewidget.insertTopLevelItem(
                qtreewidget.topLevelItemCount() - 1, qitem)

    def addfiles_src(self):
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
        items, order = self.qtreewidegt_getitems(self.ct_tree_src)
        for filename in filelist:
            if filename not in items:
                items[filename] = set()
                order.append(filename)
        for subtitle in filelist_subtitle:
            for video in order:
                if subtitle.startswith(os.path.splitext(video)[0]):
                    items[video].add(subtitle)
                    break
        self.qtreewidegt_setitems(self.ct_tree_src, items, order)
        self.ct_tree_src.resizeColumnToContents(0)

    def ct_start_clicked(self):
        print('start')

    def ct_tree_src_clicked(self, item, column):
        if self.ct_tree_src.indexOfTopLevelItem(item) + 1 == \
                self.ct_tree_src.topLevelItemCount():
            self.addfiles_src()

    def ct_tree_itemexpanded(self, item):
        self.sender().resizeColumnToContents(0)

    def ct_tree_itemcollapsed(self, item):
        self.sender().resizeColumnToContents(0)
