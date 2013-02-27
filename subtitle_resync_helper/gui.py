# -*- coding: utf-8 -*-

import sys

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QWidget, QKeySequence, QApplication
from pygs import QxtGlobalShortcut

from . import config, player
from .gui_ui import Ui_Form

Player = player.getplayer(config.playername)

class FormTimemapper(QWidget, Ui_Form):

    def __init__(self, srcfilepath, dstfilepath):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        self.filepath_src = srcfilepath
        self.filepath_dst = dstfilepath

        self.shortcut_addpart = QxtGlobalShortcut(QKeySequence("F4"))
        self.shortcut_addpart.activated.connect(self.shortcut_addpart_activated)
        self.shortcut_addpart.setEnabled(False)
        self.shortcut_addmap = QxtGlobalShortcut(QKeySequence("F5"))
        self.shortcut_addmap.activated.connect(self.shortcut_addmap_activated)
        self.shortcut_addmap.setEnabled(False)

        self.started = False

    def closeEvent(self, event):
        del self.shortcut_addpart
        del self.shortcut_addmap
        event.accept()

    def ct_switch_clicked(self):
        if not self.started:
            self.ct_switch.setText("停止")
            self.ct_switch.repaint()
            self.player_src = Player(self.filepath_src)
            self.player_dst = Player(self.filepath_dst)
            self.shortcut_addpart.setEnabled(True)
            self.shortcut_addmap.setEnabled(True)
        else:
            self.ct_switch.setText("开始")
            self.ct_switch.repaint()
            self.player_src.close()
            self.player_dst.close()
            self.shortcut_addpart.setEnabled(False)
            self.shortcut_addmap.setEnabled(False)
        self.started = not self.started

    def shortcut_addpart_activated(self):
        self.ct_list.addItem(str([self.player_src.grabtime()]))

    def shortcut_addmap_activated(self):
        self.ct_list.addItem(str([self.player_src.grabtime(),
                                  self.player_dst.grabtime()]))
