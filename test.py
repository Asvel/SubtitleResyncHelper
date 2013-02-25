# -*- coding: utf-8 -*-

import time

from subtitle_resync_helper import config, players

config.player = r'C:\app\MPC-BE\mpc-be.exe'

player = players.MPCBE(r"D:\temp\srh\test.mp4")

while True:
    time.sleep(1)
    print(player.grabtime())
