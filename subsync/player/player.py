# -*- coding: utf-8 -*-

import subprocess

from subsync import config
from subsync.time import Time


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
        return Time(s)

    def _gettime(self):
        raise NotImplementedError()

    def _settime(self, time):
        raise NotImplementedError()

    def open(self):
        if not self._opened:
            self._open()
            self._opened = True

    def close(self):
        if self._opened:
            self._close()
            self._opened = False

    @property
    def time(self):
        return self._gettime()

    @time.setter
    def time(self, value):
        self._settime(value)
