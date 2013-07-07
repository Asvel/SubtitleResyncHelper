# -*- coding: utf-8 -*-

from subsync import config, win
from subsync.player.player_mpchc import PlayerMPCHC as Player
from subsync.player.player_mpchc import CMD


class PlayerMPCBE(Player):

    def _open(self):
        super(PlayerMPCBE, self)._open()
        self._first_paused = False
        self._send_message(CMD.OPENFILE, self._filepath)

    def _generate_args(self):
        return [config.playerpath, "/new", "/slave", str(self._hwnd_listener)]

    def _parse_message(self, command, message):
        if command == CMD.PLAYMODE:
            if message == "0" and not self._first_paused:
                self._first_paused = True
                self._send_message(CMD.PLAYPAUSE)
        else:
            super(PlayerMPCBE, self)._parse_message(command, message)
