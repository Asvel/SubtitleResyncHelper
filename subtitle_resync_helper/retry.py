# -*- coding: utf-8 -*-

import time


def retry(func, initdelay=0.01, maxcount=10):
    ret = None
    for count in range(maxcount):
        time.sleep(initdelay * (2 ** count))
        try:
            ret = func()
        except:
            pass
        if ret is not None:
            break
    return ret
