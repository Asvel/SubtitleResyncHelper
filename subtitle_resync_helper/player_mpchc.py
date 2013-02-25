# -*- coding: utf-8 -*-

from . import config, win
from .player import Player


class PlayerMPCHC(Player):

    def __init__(self, filepath):
        super(PlayerMPCHC, self).__init__(filepath)
        pass

    def _generate_args(self, filepath):
        return [config.player, "/open", "/new", filepath]

    def _get_main_window_handle(self):
        return win.FindWindow("MPC-HC", None)
