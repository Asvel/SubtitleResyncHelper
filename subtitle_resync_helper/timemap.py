# -*- coding: utf-8 -*-

import datetime

from .time import Time


def normalize(timemap):
    timemap = [x for x in timemap if 1 <= len(x) <= 2] + [[Time(h=100)]]
    timedelta = []
    for i in range(len(timemap)-1):
        if len(timemap[i]) == 2:
            timedelta.append({'delta': timemap[i][1] - timemap[i][0],
                              'until': timemap[i+1][0]})
    return timedelta
