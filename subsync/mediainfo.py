# -*- coding: utf-8 -*-

import os
from collections import defaultdict

from pymediainfo import MediaInfo

from subsync import config
from subsync.util import tryfunc


__all__ = ['clear_cache', 'frame_rate']


_cache = {}


def _get_media_info(filepath):
    global _cache
    if filepath not in _cache:
        media_info = MediaInfo.parse(filepath)
        tracks = defaultdict(list)
        for track in media_info.tracks:
            tracks[track.track_type].append(track)
            tracks[track.id].append(track)
        _cache[filepath] = tracks
    return _cache[filepath]


def clear_cache():
    global _cache
    _cache = {}

    if config.mediainfodir not in os.environ['PATH']:
        os.environ['PATH'] = config.mediainfodir + os.pathsep + os.environ['PATH']

clear_cache()


def frame_rate(filepath):
    video_tracks = _get_media_info(filepath)['Video']
    return next((tryfunc(float, x.frame_rate) for x in video_tracks), None)
