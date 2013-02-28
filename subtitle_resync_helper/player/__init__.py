# -*- coding: utf-8 -*-

from subtitle_resync_helper.player.player_mpchc import PlayerMPCHC as MPCHC
from subtitle_resync_helper.player.player_mpcbe import PlayerMPCBE as MPCBE


def getplayer(name):
    return globals()[name]
