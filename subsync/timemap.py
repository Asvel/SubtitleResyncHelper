# -*- coding: utf-8 -*-

from subsync.time import Time


def normalize(timemap):
    """一般化时间映射表，生成时间偏移表"""
    timemap = [x for x in timemap if 1 <= len(x) <= 2] + [[Time(h=100)]]
    timedelta = []
    for i in range(len(timemap)-1):
        if len(timemap[i]) == 2 and timemap[i][1] is not None:
            timedelta.append({'delta': timemap[i][1] - timemap[i][0],
                              'until': timemap[i+1][0]})
    return timedelta
