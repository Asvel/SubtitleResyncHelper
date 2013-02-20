# -*- coding: utf-8 -*-

import datetime
import logging

import pysubs
from pysubs import Time

timemapfile = r"D:\temp\srh\timemap.txt"
fni = r"D:\temp\srh\test.ass"
fno = r"D:\temp\srh\testo.ass"

SHIFT_STOP = 0      # 停止并返回
SHIFT_APART = 1     # 分别按各自的调整量调整
SHIFT_BY_START = 2  # 按开始时间的调整量调整
SHIFT_BY_END = 3    # 按结束时间的调整量调整


# 时间相差小于0.04s忽略不计
def _time_eq(self, other):
    if isinstance(other, Time):
        return abs(self.ms_time - other.ms_time) <= 40
    else:
        return NotImplemented
Time.__eq__ = _time_eq

def parse_time(s):
    t = None
    for fmt in ["%M:%S.%f","%H:%M:%S.%f",]:
        try:
            t = datetime.datetime.strptime(s, fmt).time()
            break
        except:
            pass
    if t is None:
        raise Exception("无法解析时间 {}".format(s))
    return Time(h=t.hour, m=t.minute, s=t.second, ms=t.microsecond//1000)

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

def generate_timedelta(timemap):
    timemap = [x for x in timemap if 1 <= len(x) <= 2] + [[Time(h=100)]]
    timedelta = []
    for i in range(len(timemap)-1):
        if len(timemap[i]) == 2:
            timedelta.append({'delta': timemap[i][1] - timemap[i][0],
                'until': timemap[i+1][0]})
    return timedelta

logging.basicConfig(format='%(levelname)s\t: %(message)s', level=logging.DEBUG)

timemap = []
with open(timemapfile, encoding='utf-8') as f:
    for line in f:
        timemap.append([parse_time(x) for x in line.split()])

timedelta = generate_timedelta(timemap)

subs = pysubs.load(fni, encoding='utf-8')
shift(subs, timedelta)
subs.save(fno)
