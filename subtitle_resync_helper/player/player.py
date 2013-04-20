# -*- coding: utf-8 -*-

import subprocess

from subtitle_resync_helper import config, time


class Player(object):

    def __init__(self, filepath, autoopen=True):
        self._filepath = filepath
        self._opened = False
        if autoopen:
            self.open()

    def __del__(self):
        self.close()

    def _generate_args(self):
        return [config.playerpath, self._filepath]

    def _open(self):
        self._player = subprocess.Popen(self._generate_args())

    def _close(self):
        self._player.terminate()

    def _parse_time(self, s):
        return time.parse(s)

    def open(self):
        if not self._opened:
            self._open()
            self._opened = True

    def grabtime(self):
        raise NotImplementedError()

    def close(self):
        if self._opened:
            self._close()
            self._opened = False
