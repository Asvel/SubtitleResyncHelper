# -*- coding: utf-8 -*-

import sys

from PyQt4.QtGui import QApplication

from subtitle_resync_helper import config
config.playerpath = r'C:\app\MPC-BE\mpc-be.exe'
config.playername = "MPCBE"

from subtitle_resync_helper import gui

app = QApplication(sys.argv)
window = gui.FormTimemapper(r"D:\temp\srh\src.mkv", r"D:\temp\srh\dst.mkv")

window.show()
sys.exit(app.exec())
