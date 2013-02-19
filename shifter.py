
import datetime
import pysubs

timemapfile = r"D:\temp\srh\timemap.txt"
subtitlefile = r"D:\temp\srh\test.ass"


def parse_time(s):
    time = None
    for fmt in ["%M:%S.%f","%H:%M:%S.%f",]:
        try:
            time = datetime.datetime.strptime(s, fmt).time()
            break
        except:
            pass
    if time is None:
        raise Exception("无法解析时间 {}".format(s))
    return time

timemap = []
with open(timemapfile, encoding='utf-8') as f:
    for line in f:
        timemap.append([parse_time(x) for x in line.split()])

subs = pysubs.load(subtitlefile, encoding='utf-8')
for line in subs:
    print(line)
