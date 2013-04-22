# -*- coding: utf-8 -*-

import logging

from subtitle_resync_helper import time
from subtitle_resync_helper.time import Time


def normalize(timemap, endcheck=False):
    """一般化时间映射表，生成时间偏移表

    endcheck 是否包含结尾校验
    """
    timemap = [x for x in timemap if 1 <= len(x) <= 2] + [[Time(h=100)]]
    timedelta = []
    for i in range(len(timemap)-1):
        if len(timemap[i]) == 2 and timemap[i][1] is not None:
            timedelta.append({'delta': timemap[i][1] - timemap[i][0],
                              'until': timemap[i+1][0]})
    if endcheck:
        if time.is_approx_equal(timedelta[-1]['delta'], timedelta[-2]['delta']):
            del timedelta[-2]
        else:
            logging.error("结尾校验没有通过，可能存在遗漏的时间映射")
            raise Exception("结尾校验没有通过")
    return timedelta
