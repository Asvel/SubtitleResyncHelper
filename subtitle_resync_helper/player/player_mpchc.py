# -*- coding: utf-8 -*-

import re
from time import sleep

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
        hwnds = win.FindWindows(class_="#32770", parent=self._mainhwnd)
        for hwnd in hwnds:
            win.SendMessage(hwnd, win.WM_CLOSE, 0, 0)
        if len(hwnds) > 0:
            sleep(0.1)
        win.SendKey(self._mainhwnd, "Ctrl+G")
        hwnd = retry(lambda:win.FindWindows(
            class_="#32770", parent=self._mainhwnd)[0], maxcount=6)
        if hwnd is None:
            win.SendKey(self._mainhwnd, "Ctrl+G")
            hwnd = retry(lambda:win.FindWindows(
                class_="#32770", parent=self._mainhwnd)[0])
        edit = retry(lambda:win.FindWindows(
            class_='Edit', parent=hwnd, top_level=False)[0])
        text = win.GetWindowTextX(edit)
        try:
            match = re.match(r"^(\d+?), (\d+\.?\d*)$", text)
            time = Time(frame=int(match.group(1)), fps=float(match.group(2)))
        finally:
            for hwnd in win.FindWindows(class_="#32770", parent=self._mainhwnd):
                win.SendMessage(hwnd, win.WM_CLOSE, 0, 0)
        return time

    def close(self):
        win.CloseHandle(self._handle)
        for hwnd in win.FindWindows(parent=self._mainhwnd):
            win.SendMessage(hwnd, win.WM_CLOSE, 0, 0)
        win.PostMessage(self._mainhwnd, win.WM_CLOSE, 0, 0)
        self._closed = True
