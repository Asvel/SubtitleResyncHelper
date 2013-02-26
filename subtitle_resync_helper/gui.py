# -*- coding: utf-8 -*-

import sys

from PyQt4.QtGui import QDialog, QKeySequence
from pygs import QxtGlobalShortcut

from . import config, player
from .gui_ui import Ui_Form

Player = player.getplayer(config.playername)

class FormTimemapper(QDialog, Ui_Form):

    def __init__(self, srcfilepath, dstfilepath):
        QDialog.__init__(self)
        self.setupUi(self)

        self.filepath_src = srcfilepath
        self.filepath_dst = dstfilepath

        self.shortcut_addpart = QxtGlobalShortcut(QKeySequence("F4"))
        self.shortcut_addpart.activated.connect(self.shortcut_addpart_activated)
        self.shortcut_addpart.setDisabled()

        self.shortcut_addmap = QxtGlobalShortcut(QKeySequence("F5"))
        self.shortcut_addmap.activated.connect(self.shortcut_addmap_activated)
        self.shortcut_addmap.setDisabled()

    def __del__(self):
        del self.shortcut_addpart
        del self.shortcut_addmap

    def ct_switch_clicked(self):
        self.player_src = Player(self.filepath_src)
        self.player_dst = Player(self.filepath_dst)

        self.shortcut_addpart.setEnabled()
        self.shortcut_addmap.setEnabled()

    def shortcut_addpart_activated(self):
        self.ct_list.addItem(str([self.player_src.grabtime()]))

    def shortcut_addmap_activated(self):
        self.ct_list.addItem(str([self.player_src.grabtime(),
                                  self.player_dst.grabtime()]))
