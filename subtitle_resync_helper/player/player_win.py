# -*- coding: utf-8 -*-

from subtitle_resync_helper import config, win
from subtitle_resync_helper.player.player import Player


class PlayerWin(Player):

    def _open(self):
        super(PlayerWin, self)._open()

        handle = win.GetProcessHandleByProcessId(self._player.pid)
        win.WaitForInputIdle(handle, win.INFINITE)
        win.CloseHandle(handle)

        self._mainhwnd = self._get_main_window_handle()
        win.MaximumWindow(self._mainhwnd)

    def _get_main_window_handle(self):
        raise NotImplementedError()

    def _close(self):
        for hwnd in win.FindWindows(parent=self._mainhwnd):
            win.SendMessage(hwnd, win.WM_CLOSE, 0, 0)
        win.PostMessage(self._mainhwnd, win.WM_CLOSE, 0, 0)

    def grabtime(self):
        hwnd = win.GetGUIThreadInfo(0).hwndFocus
        text = win.GetWindowTextX(hwnd).strip()
        try:
            time = self._parse_time(text)
        except:
            time = None
        return time
