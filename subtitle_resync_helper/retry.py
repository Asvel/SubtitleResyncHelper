# -*- coding: utf-8 -*-

import time


def retry(func, initdelay=0.01, maxcount=10):
    count = 0
    while count < maxcount:
        time.sleep(initdelay * (2 ** count))
        ret = func()
        if ret is not None:
            return ret
        count += 1
    return None
