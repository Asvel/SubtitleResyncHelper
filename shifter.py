
import datetime
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

timemap = []
with open(timemapfile, encoding='utf-8') as f:
    for line in f:
        timemap.append([parse_time(x) for x in line.split()])

timemap = [x for x in timemap if 1 <= len(x) <= 2]
timemap.append([Time(h=100)])
for i in range(len(timemap)-1):
    if len(timemap[i]) == 2:
        timemap[i][1] -= timemap[i][0]  # offset
        timemap[i][0] = timemap[i+1][0] # until
timemap = [x for x in timemap if len(x) == 2]

subs = pysubs.load(fni, encoding='utf-8')
for line in subs:
    timemap_start = next(x for x in timemap if x[0] > line.start)
    timemap_end = next(x for x in timemap if x[0] > line.end)
    if timemap_start != timemap_end:
        raise Exception("timemap_start != timemap_end")
    line.start += timemap_start[1]
    line.end += timemap_end[1]

subs.save(fno)
