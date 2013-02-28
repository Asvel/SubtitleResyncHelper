# -*- coding: utf-8 -*-

import sys

from PyQt4.QtCore import Qt
from PyQt4.QtGui import (QWidget, QKeySequence, QApplication,
                         QTableWidgetItem, QHeaderView)
from pygs import QxtGlobalShortcut

from . import config, player
from .gui_ui import Ui_Form

Player = player.getplayer(config.playername)

class FormTimemapper(QWidget, Ui_Form):

    def __init__(self, fileinfos):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.move(0, 0)

        self.fileinfos = fileinfos

        self.ct_table.setRowCount(0)
        self.ct_table.setColumnCount(len(self.fileinfos))
        self.ct_table.horizontalHeader().setResizeMode(
            QHeaderView.ResizeToContents)

    def showEvent(self, event):
        self.shortcut_addpart = QxtGlobalShortcut(QKeySequence("F4"))
        self.shortcut_addpart.activated.connect(self.shortcut_addpart_activated)
        self.shortcut_addmap = QxtGlobalShortcut(QKeySequence("F5"))
        self.shortcut_addmap.activated.connect(self.shortcut_addmap_activated)

        self.players = [Player(x['path']) for x in self.fileinfos]

    def closeEvent(self, event):
        del self.shortcut_addpart
        del self.shortcut_addmap
        for p in self.players:
            p.close()
        event.accept()

    def grabtimes(self, src_only=False):
        count = self.ct_table.rowCount()
        self.ct_table.setRowCount(count + 1)
        for i in range(len(self.fileinfos)):
            if src_only and self.fileinfos[i]['type'] != "src":
                text = ""
            else:
                text = str(self.players[i].grabtime())
            self.ct_table.setItem(count, i, QTableWidgetItem(text))

    def shortcut_addpart_activated(self):
        self.grabtimes(src_only=True)

    def shortcut_addmap_activated(self):
        self.grabtimes()
