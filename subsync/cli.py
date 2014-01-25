# -*- coding: utf-8 -*-

import sys
import logging
import argparse

from subsync import subtitle
from subsync.time import Time


def run(args=sys.argv):

    class ArgumentParser(argparse.ArgumentParser):
        def format_usage(self):
            return argparse.ArgumentParser.format_usage(self) \
                .replace("usage:", "用法：")
        def format_help(self):
            return argparse.ArgumentParser.format_help(self) \
                .replace("usage:", "用法：") \
                .replace("positional arguments:", "参数：") \
                .replace("\n\noptional arguments:", "") \
                .replace("show this help message and exit", "显示此帮助并退出")

    parser = ArgumentParser(
        description='根据时间映射表调整字幕时间轴',
        epilog="""\
""",
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('timemap', help="时间映射表文件名")
    parser.add_argument('source', help="原始字幕文件")
    parser.add_argument('result', help="调整后的字幕文件")
    parser.add_argument('-l', '--loglevel', default='info',
                        choices=['none', 'error', 'warning', 'info', 'debug'],
                        help="输出信息的等级，默认为 info")
    parser.add_argument('-d', '--diffdeltahandle', default='apart',
                        choices=['falied', 'apart', 'start', 'end'],
                        help="开始结束时间调整量不同的处理方法，默认为 apart")
    args = parser.parse_args(args)

    ftm = args.timemap
    fni = args.source
    fno = args.result

    loglevel = getattr(logging, args.loglevel.upper(), logging.CRITICAL)
    logging.basicConfig(format='%(levelname)s\t: %(message)s', level=loglevel)

    diffdeltahandledict = {
        'falied': subtitle.SHIFT_FAILED,
        'apart': subtitle.SHIFT_APART,
        'start': subtitle.SHIFT_BY_START,
        'end': subtitle.SHIFT_BY_END,
    }
    diff_delta_handler = diffdeltahandledict[args.diffdeltahandle]

    timemap = []
    with open(ftm, encoding='utf-8') as f:
        for line in f:
            timemap.append([Time(x) for x in line.split()])

    subtitle.shift(fni, fno, None, timemap, diff_delta_handler)
