# -*- coding: utf-8 -*-

import json
from time import sleep

__all__ = ['tryfunc', 'retryfunc', 'is_approx_equal', 'dump_readable_json']


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


class _ReadableJsonEncoder(json.JSONEncoder):
    def __init__(self, single_line):
        intdent = None if single_line else '\t'
        super().__init__(ensure_ascii=False, check_circular=False, sort_keys=True, indent=intdent)

    def default(self, o):
        from subsync.time import Time
        if isinstance(o, Time):
            return repr(o)
        else:
            return json.JSONEncoder.default(self, o)

_readable_json_encoder_singleline = _ReadableJsonEncoder(True)
_readable_json_encoder_multiline = _ReadableJsonEncoder(False)


def dump_readable_json(obj, single_line=False):
    """生成人类易读（少转义、键有序）的 JSON 串

    obj 要生成 JSON 的对象
    single_line 为 True 时生成单行的 JSON，否则生成多行的 JSON
    """
    if single_line:
        return _readable_json_encoder_singleline.encode(obj)
    else:
        return _readable_json_encoder_multiline.encode(obj)
