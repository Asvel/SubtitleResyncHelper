# -*- coding: utf-8 -*-

from time import sleep


__all__ = ['tryfunc', 'retryfunc', 'is_approx_equal']


def tryfunc(func, *args, default=None):
    """尝试执行函数 func，发生异常时返回 default 的值"""
    try:
        return func(*args)
    except Exception:
        return default


def retryfunc(func, *args, initdelay=0.01, maxcount=10):
    """反复尝试执行函数 func，直到返回 true 或到达次数上限，每次尝试之后延时加倍"""
    ret = None
    for count in range(maxcount):
        sleep(initdelay)
        try:
            ret = func()
        except Exception:
            pass
        if ret:
            break
        initdelay *= 2
    return ret


def is_approx_equal(a, b, tolerance=None):
    """是否约等于，判断 a 和 b 之间的差是否小于 tolerance"""
    return abs(a - b) < tolerance if tolerance else a == b
