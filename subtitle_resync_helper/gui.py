# -*- coding: utf-8 -*-

import sys

from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog, QKeySequence
from pygs import QxtGlobalShortcut

from .gui_ui import Ui_Form


class Form(QDialog, Ui_Form):

    def __init__(self):
        QDialog.__init__(self)

        # Set up the user interface from Designer.
        self.setupUi(self)

    def __del__(self):
        del self.shortcut

    def ct_switch_clicked(self):
        self.shortcut = QxtGlobalShortcut()
        self.shortcut.setShortcut(QKeySequence("F5"))
        self.shortcut.activated.connect(self.shortcut_activated)

    def shortcut_activated(self):
        print("hello")
        self.ct_list.addItem("hello")
