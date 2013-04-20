# -*- coding: utf-8 -*-

from subtitle_resync_helper import config, win
from subtitle_resync_helper.player.player import Player


class PlayerWin(Player):

    def _open(self):
        super(PlayerWin, self)._open()

        handle = win.GetProcessHandleByProcessId(self._player.pid)
        win.WaitForInputIdle(handle, win.INFINITE)
        win.CloseHandle(handle)

        self._hwnd = self._get_main_window_handle()
        win.MaximumWindow(self._hwnd)

    def _get_main_window_handle(self):
        raise NotImplementedError()

    def _close(self):
        for hwnd in win.FindWindows(parent=self._hwnd):
            win.SendMessage(hwnd, win.WM_CLOSE, 0, 0)
        win.PostMessage(self._hwnd, win.WM_CLOSE, 0, 0)

    def grabtime(self):
        hwnd = win.GetGUIThreadInfo(0).hwndFocus
        text = win.GetWindowTextX(hwnd).strip()
        try:
            time = self._parse_time(text)
        except Exception:
            time = None
        return time

    def focus(self):
        win.SetForegroundWindow(self._hwnd)

    @property
    def has_focus(self):
        return self._hwnd == win.GetForegroundWindow()
