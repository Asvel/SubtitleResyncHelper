# -*- coding: utf-8 -*-

from itertools import zip_longest

from subsync import player, config
from subsync.time import Time, is_approx_equal

tolerance = player.getplayer(config.playertype).timedelta_tolerance


def normalize(timemap):
    """一般化时间映射表，生成时间偏移表"""
    timemap = [item for item in timemap if 1 <= len(item) <= 2]
    timedelta = []
    for item, next_ in zip_longest(timemap, timemap[1:], fillvalue=[Time(h=100)]):
        if len(item) == 2 and item[1] is not None:
            timedelta.append({'delta': item[1]-item[0], 'until': next_[0]})
    averaged = []
    while timedelta:
        i = 0
        for (i, item), next_ in zip_longest(enumerate(timedelta), timedelta[1:]):
            if next_ and not is_approx_equal(item['delta'], next_['delta'], tolerance):
                break
        average_delta = sum(map(lambda x: x['delta'], timedelta[:i+1]), Time.zero) / (i+1)
        if abs(average_delta.ms_time)  < tolerance:
            average_delta = Time.zero
        averaged.append({'delta': average_delta, 'until': timedelta[i]['until']})
        timedelta = timedelta[i+1:]
    return averaged
