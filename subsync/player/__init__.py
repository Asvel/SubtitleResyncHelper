# -*- coding: utf-8 -*-

from subsync.player.player_mpchc import PlayerMPCHC as MPCHC
from subsync.player.player_mpcbe import PlayerMPCBE as MPCBE


def getplayer(type):
    return globals()[type]
