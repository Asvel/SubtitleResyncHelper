# -*- coding: utf-8 -*-

import subprocess

from subtitle_resync_helper import config, time, win


class Player(object):

    def __init__(self, filepath):
        self._closed = False
        self._player = subprocess.Popen(self._generate_args(filepath))
        self._handle = win.GetProcessHandleByProcessId(self._player.pid)
        self._prepare()

    def __del__(self):
        if not self._closed:
            self.close()

    def _generate_args(self, filepath):
        return [config.playerpath, filepath]

    def _prepare(self):
        win.WaitForInputIdle(self._handle, win.INFINITE)
        self._mainhwnd = self._get_main_window_handle()
        win.MaximumWindow(self._mainhwnd)

    def _get_main_window_handle(self):
        raise NotImplementedError()

    def _parse_time(self, s):
        return time.parse(s)

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
