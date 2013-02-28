# -*- coding: utf-8 -*-

import logging

from subtitle_resync_helper.time import Time

SHIFT_STOP = 0      # 停止并返回
SHIFT_APART = 1     # 分别按各自的调整量调整
SHIFT_BY_START = 2  # 按开始时间的调整量调整
SHIFT_BY_END = 3    # 按结束时间的调整量调整


def shift(subs, timedelta, diffdeltahandle=SHIFT_APART):
    for line in subs:
        delta_start = next(x for x in timedelta
            if line.start < x['until'])['delta']
        delta_end = next(x for x in timedelta
            if line.end < x['until'])['delta']
        if delta_start != delta_end:
            logging.warning("字幕 {} 的开始时间与结束时间调整量不同"
                            .format(str(line)))
            if diffdeltahandle == SHIFT_STOP:
                raise Exception("开始时间与结束时间调整量不同")
            elif diffdeltahandle == SHIFT_APART:
                pass
            elif diffdeltahandle == SHIFT_BY_START:
                delta_end = delta_start
            elif diffdeltahandle == SHIFT_BY_END:
                delta_start = delta_end
        line.start += delta_start
        if line.start < Time.zero:
            line.start = Time.zero
            logging.warning("字幕 {} 的开始时间调整后小于0".format(str(line)))
        line.end += delta_end
        if line.end < Time.zero:
            line.end = Time.zero
            logging.warning("字幕 {} 的结束时间调整后小于0".format(str(line)))
