# -*- coding: utf-8 -*-

import sys

from PyQt4.QtGui import QApplication

from subsync import config, gui

app = QApplication(sys.argv)
window = gui.FormMain()

window.show()
ret = app.exec()

config._save()

sys.exit(ret)
