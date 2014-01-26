# -*- coding: utf-8 -*-

import os as _os
import sys as _sys
import logging as _logging
import json as _json


playerpath = ""
playertype = None

mediainfodir = ""

filedialog_lastdir = ""

fileext_video = ["mkv", "mp4"]
fileext_subtitle = ["ass", "ssa", "srt"]

shortcut = {
    'main_start': 'F2',
    'timemapper_addpart': 'F4',
    'timemapper_addmap': 'F5',
    'timemapper_dellast': 'F9',
    'timemapper_finish': 'F11',
    'timemapper_next': 'Tab',
    'timemapper_next_with_time': 'Ctrl+Tab',
}

timemapper_color = [
    ('#111', '#FFF'),
    ('#111', '#CCC')
]


_config_path = _os.path.join(_os.path.dirname(_sys.argv[0]), "config.json")


def _load():
    if _os.path.exists(_config_path):
        with open(_config_path, encoding='utf-8') as f:
            config = _json.load(f)
        global_ = globals()
        for k in global_:
            if not k.startswith('_') and k in config:
                if isinstance(global_[k], dict):
                    global_[k].update(config[k])
                else:
                    global_[k] = config[k]
    else:
        _logging.warning("配置文件 {} 无法访问，使用默认配置".format(
            _config_path))
_load()


def _save():
    config = {}
    for k, v in globals().items():
        if not k.startswith('_'):
            config[k] = v
    with open(_config_path, mode='w', encoding='utf-8') as f:
        _json.dump(config, f, ensure_ascii=False, indent='\t', sort_keys=True)
