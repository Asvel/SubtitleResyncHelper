# -*- coding: utf-8 -*-

from . import config, win
from .player_mpchc import PlayerMPCHC as Player


class PlayerMPCBE(Player):

    def __init__(self, filepath):
        super(PlayerMPCBE, self).__init__(filepath)
        pass

    def _get_main_window_handle(self):
        return win.FindWindow("MPC-BE", None)
