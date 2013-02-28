# -*- coding: utf-8 -*-

import sys
import time

from PyQt4.QtGui import QApplication

from subtitle_resync_helper import config
config.playerpath = r'C:\app\MPC-BE\mpc-be.exe'
config.playername = "MPCBE"

from subtitle_resync_helper import gui

app = QApplication(sys.argv)
window = gui.FormTimemapper([
    {'type':'src', 'path':r"D:\temp\srh\src.mkv"},
    {'type':'dst', 'path':r"D:\temp\srh\dst.mkv"},
    ])

def printlist(l):
    print("\n".join(map(str, l)))

window.finished.connect(printlist)

window.show()
sys.exit(app.exec())
