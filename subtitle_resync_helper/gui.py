# -*- coding: utf-8 -*-

import sys

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QWidget, QKeySequence, QApplication, QTableWidgetItem
from pygs import QxtGlobalShortcut

from . import config, player
from .gui_ui import Ui_Form

Player = player.getplayer(config.playername)

class FormTimemapper(QWidget, Ui_Form):

    def __init__(self, fileinfos):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        self.fileinfos = fileinfos

        self.shortcut_addpart = QxtGlobalShortcut(QKeySequence("F4"))
        self.shortcut_addpart.activated.connect(self.shortcut_addpart_activated)
        self.shortcut_addpart.setEnabled(False)
        self.shortcut_addmap = QxtGlobalShortcut(QKeySequence("F5"))
        self.shortcut_addmap.activated.connect(self.shortcut_addmap_activated)
        self.shortcut_addmap.setEnabled(False)

        self.started = False

        self.ct_table.setRowCount(0)
        self.ct_table.setColumnCount(len(self.fileinfos))

    def closeEvent(self, event):
        del self.shortcut_addpart
        del self.shortcut_addmap
        event.accept()

    def ct_switch_clicked(self):
        if not self.started:
            self.ct_switch.setText("停止")
            self.ct_switch.repaint()
            self.players = [Player(x['path']) for x in self.fileinfos]
            self.shortcut_addpart.setEnabled(True)
            self.shortcut_addmap.setEnabled(True)
        else:
            self.ct_switch.setText("开始")
            self.ct_switch.repaint()
            for p in self.players:
                p.close()
            self.shortcut_addpart.setEnabled(False)
            self.shortcut_addmap.setEnabled(False)
        self.started = not self.started

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
