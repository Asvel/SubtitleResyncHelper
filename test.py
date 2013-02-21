# -*- coding: utf-8 -*-

import logging

import pysubs

from subtitle_resync_helper import time, timemap, shifter

timemapfile = r"D:\temp\srh\timemap.txt"
fni = r"D:\temp\srh\test.ass"
fno = r"D:\temp\srh\testo.ass"

logging.basicConfig(format='%(levelname)s\t: %(message)s', level=logging.DEBUG)

tmap = []
with open(timemapfile, encoding='utf-8') as f:
    for line in f:
        tmap.append([time.parse(x) for x in line.split()])

timedelta = timemap.normalize(tmap)

subs = pysubs.load(fni, encoding='utf-8')
shifter.shift(subs, timedelta)
subs.save(fno)
