# -*- coding: utf-8 -*-

import time


def retry(func, initdelay=0.01, maxcount=10):
    """反复尝试 func 直到返回 true 或到达次数上限，每次尝试之后延时加长"""
    ret = None
    for count in range(maxcount):
        time.sleep(initdelay * (2 ** count))
        try:
            ret = func()
        except Exception:
            pass
        if ret:
            break
    return ret
