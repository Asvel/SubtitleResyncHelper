# -*- coding: utf-8 -*-

from pysubs import Time

from subsync import util


def is_approx_equal(time1, time2, tolerance=20):
    """判断两个时间是否近似相等"""
    if isinstance(tolerance, int):
        tolerance = Time(ms=tolerance)
    return util.is_approx_equal(time1, time2, tolerance)
