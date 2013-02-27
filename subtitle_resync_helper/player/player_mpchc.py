# -*- coding: utf-8 -*-

import re

from .. import config, win
from ..retry import retry
from ..time import Time
from .player import Player


class PlayerMPCHC(Player):

    def __init__(self, filepath):
        super(PlayerMPCHC, self).__init__(filepath)
        pass

    def _generate_args(self, filepath):
        return [config.playerpath, "/open", "/new", filepath]

    def _get_main_window_handle(self):
        return win.FindWindow("MPC-HC", None)

    def grabtime(self):
        win.SendKey(self._mainhwnd, "Ctrl+G")
        hwnd = retry(lambda:(win.FindWindows(class_="#32770",
                                             parent=self._mainhwnd) + [None])[0])
        edit = retry(lambda:(win.FindWindows(class_='Edit',
                                             parent=hwnd, top_level=False) + [None])[0])
        text = win.GetWindowTextByHwnd(edit)
        match = re.match(r"^(\d+?), (\d+\.?\d*)$", text)
        time = Time(frame=int(match.group(1)), fps=float(match.group(2)))
        win.SendKey(hwnd, "Esc")
        return time
