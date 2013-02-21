# -*- coding: utf-8 -*-

import datetime

import pysubs


class Time(pysubs.Time):
    """忽略小于0.04s时间差的 pysubs.Time 类"""

    def _time_eq(self, other):
        if isinstance(other, Time) or isinstance(other, pysubs.Time):
            return abs(self.ms_time - other.ms_time) < 40
        else:
            return NotImplemented

    def _time_ne(self, other):
        if isinstance(other, Time) or isinstance(other, pysubs.Time):
            return abs(self.ms_time - other.ms_time) >= 40
        else:
            return NotImplemented


def parse(s):
    t = None
    for fmt in ["%M:%S.%f", "%H:%M:%S.%f"]:
        try:
            t = datetime.datetime.strptime(s, fmt).time()
            break
        except Exception:
            pass
    if t is None:
        raise Exception("无法解析时间 {}".format(s))
    return Time(h=t.hour, m=t.minute, s=t.second, ms=t.microsecond//1000)
