# -*- coding: utf-8 -*-

import time


def retry(func, initdelay=0.01, maxcount=10):
    count = 0
    ret = None
    while count < maxcount:
        time.sleep(initdelay * (2 ** count))
        try:
            ret = func()
        except:
            pass
        if ret is not None:
            break
        count += 1
    return ret
