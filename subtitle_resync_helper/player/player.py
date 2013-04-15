# -*- coding: utf-8 -*-

import subprocess

from subtitle_resync_helper import config, time


class Player(object):

    def __init__(self, filepath):
        self._closed = False
        self._player = subprocess.Popen(self._generate_args(filepath))

    def __del__(self):
        if not self._closed:
            self.close()

    def _generate_args(self, filepath):
        return [config.playerpath, filepath]

    def _parse_time(self, s):
        return time.parse(s)

    def grabtime(self):
        raise NotImplementedError()

    def close(self):
        self._player.terminate()
        self._closed = True
