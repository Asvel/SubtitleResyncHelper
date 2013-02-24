# -*- coding: utf-8 -*-

import sys

from PyQt4.QtGui import QApplication

from subtitle_resync_helper import gui

app = QApplication(sys.argv)
window = gui.Form()

window.show()
sys.exit(app.exec())
