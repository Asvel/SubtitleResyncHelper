# -*- coding: utf-8 -*-

import datetime
import logging

import pysubs
from pysubs import Time

timemapfile = r"D:\temp\srh\timemap.txt"
fni = r"D:\temp\srh\test.ass"
fno = r"D:\temp\srh\testo.ass"


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

def shift(subs, offsets):
    for line in subs:
        timemap_start = next(x for x in offsets if line.start < x['until'])
        timemap_end = next(x for x in offsets if line.end < x['until'])
        if timemap_start != timemap_end:
            logging.warning("字幕 {} 的开始时间与结束时间对应不同的时间映射"
                            .format(str(line)))
            raise Exception("timemap_start != timemap_end")
        line.start += timemap_start['delta']
        if line.start < Time.zero:
            line.start = Time.zero
            logging.warning("字幕 {} 的开始时间调整后小于0".format(str(line)))
        line.end += timemap_end['delta']
        if line.end < Time.zero:
            line.end = Time.zero
            logging.warning("字幕 {} 的结束时间调整后小于0".format(str(line)))

def generate_timedelta(timemap):
    timemap = [x for x in timemap if 1 <= len(x) <= 2] + [[Time(h=100)]]
    offsets = []
    for i in range(len(timemap)-1):
        if len(timemap[i]) == 2:
            offsets.append({'delta': timemap[i][1] - timemap[i][0],
                'until': timemap[i+1][0]})
    return offsets

logging.basicConfig(format='%(levelname)s\t: %(message)s', level=logging.DEBUG)

timemap = []
with open(timemapfile, encoding='utf-8') as f:
    for line in f:
        timemap.append([parse_time(x) for x in line.split()])

subs = pysubs.load(fni, encoding='utf-8')
timedelta = generate_timedelta(timemap)
shift(subs, timedelta)
subs.save(fno)
