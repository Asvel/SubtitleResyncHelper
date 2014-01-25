# -*- coding: utf-8 -*-

import logging
from os import path

import pysubs

import subsync
from subsync import config, time, timemap
from subsync.time import Time
from subsync.util import dump_readable_json


SHIFT_FAILED = 'SHIFT_FAILED'      # 平移失败，抛出异常
SHIFT_APART = 'SHIFT_APART'        # 分别按各自的平移量平移
SHIFT_BY_START = 'SHIFT_BY_START'  # 按开始时间的平移量平移
SHIFT_BY_END = 'SHIFT_BY_END'      # 按结束时间的平移量平移


class Subtitle:
    """字幕处理

    平移时间轴、添加平移信息
    """

    def __init__(self, filepath):
        """打开字幕 filepath 准备处理"""
        self._filepath = filepath
        self._subs = pysubs.load(filepath)
        self._timemap = None
        self._timedelta = None

    def shift(self, timedelta=None, diff_delta_handler=SHIFT_APART):
        """根据时间偏移表 timedelta 平移字幕的时间轴

        diff_delta_handler 开始时间与结束时间偏移量不同时的处理方式
        """
        self._timedelta = timedelta
        if len(timedelta) > 0:
            for line in self._subs:
                # 确定这条字幕的起止时间对应的偏移量
                delta_start = next(x for x in timedelta if line.start < x['until'])['delta']
                delta_end = next(x for x in timedelta if line.end < x['until'])['delta']

                # 处理起止时间偏移量不同
                if not time.is_approx_equal(delta_start, delta_end):
                    logging.warning("字幕 {} 的开始时间与结束时间平移量不同".format(str(line)))
                    if diff_delta_handler == SHIFT_FAILED:
                        raise Exception("开始时间与结束时间平移量不同")
                    elif diff_delta_handler == SHIFT_APART:
                        pass
                    elif diff_delta_handler == SHIFT_BY_START:
                        delta_end = delta_start
                    elif diff_delta_handler == SHIFT_BY_END:
                        delta_start = delta_end

                # 平移！
                line.start += delta_start
                line.end += delta_end

                # 处理平移后时间小于 0
                is_not_zero_length = line.start != line.end  # 对 0 时长的字幕不发出警告
                if line.start < Time.zero:
                    line.start = Time.zero
                    if is_not_zero_length:
                        logging.warning("字幕 {} 的开始时间平移后小于0".format(str(line)))
                if line.end < Time.zero:
                    line.end = Time.zero
                    if is_not_zero_length:
                        logging.warning("字幕 {} 的结束时间平移后小于0".format(str(line)))
        else:
            logging.warning("时间偏移表为空")

    def set_resync_info(self, source_media_path, target_media_path):
        """在字幕中设置调整信息

        调整信息包括 调整信息版本、源媒体、目的媒体、源字幕、平移时间偏移表
        """
        info = {
            'version': 'subsync-' + subsync.__version__,
            'media_player': config.playername,
            'source_media': path.basename(source_media_path),
            'target_media': path.basename(target_media_path),
            'source_subtitle': path.basename(self._filepath),
            'shift_delta': self._timedelta,
        }

        if 'Resync' in self._subs.info:
            info['resync_history'] = self._subs.info['Resync']

        self._subs.info['Resync'] = dump_readable_json(info, single_line=True)

    def save_as(self, filepath):
        """保存字幕至 filepath"""
        self._subs.save(filepath)


def shift(source_sub_path, target_sub_path, timedelta=None, timemap_=None,
          diff_delta_handler=SHIFT_APART, source_media_path=None, target_media_path=None):
    """平移一个字幕的时间轴

    source_sub_path 源字幕路径
    target_sub_path 目标字幕路径
    source_media_path 源媒体路径
    target_media_path 目标媒体路径

    timedelta 时间偏移表
    timemap_ 时间映射表
    当 timedelta 为 None 时会使用 timemap_ 生成 timedelta

    diff_delta_handler 开始时间与结束时间偏移量不同时的处理方式
    """
    if timedelta is None:
        timedelta = timemap.normalize(timemap_)

    subs = Subtitle(source_sub_path)
    subs.shift(timedelta, diff_delta_handler)
    subs.set_resync_info(source_media_path, target_media_path)
    subs.save_as(target_sub_path)
