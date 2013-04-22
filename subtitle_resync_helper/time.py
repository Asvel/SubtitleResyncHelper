# -*- coding: utf-8 -*-

import datetime

from pysubs import Time


def parse(s):
    """尝试解析时间字符串"""
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


def is_approx_equal(time1, time2):
    """判断两个时间是否近似相等"""
    return abs(time1.ms_time - time2.ms_time) < 20
