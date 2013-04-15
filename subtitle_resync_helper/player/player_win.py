# -*- coding: utf-8 -*-

from subtitle_resync_helper import config, win
from subtitle_resync_helper.player.player import Player


class PlayerWin(Player):

    def __init__(self, filepath):
        super(PlayerWin, self).__init__(filepath)
        self._handle = win.GetProcessHandleByProcessId(self._player.pid)
        win.WaitForInputIdle(self._handle, win.INFINITE)
        self._mainhwnd = self._get_main_window_handle()
        win.MaximumWindow(self._mainhwnd)

    def _get_main_window_handle(self):
        raise NotImplementedError()

    def grabtime(self):
        hwnd = win.GetGUIThreadInfo(0).hwndFocus
        text = win.GetWindowTextX(hwnd).strip()
        try:
            time = self._parse_time(text)
        except:
            time = None
        return time

    def close(self):
        win.CloseHandle(self._handle)
        self._player.terminate()
        self._closed = True
