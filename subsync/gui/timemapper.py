# -*- coding: utf-8 -*-

import logging
from itertools import cycle

from PyQt4.QtCore import Qt, pyqtSignal
from PyQt4.QtGui import (QDialog, QKeySequence, QTableWidgetItem, QHeaderView,
                         QMessageBox, QColor, QBrush, QItemSelectionModel)
from pygs import QxtGlobalShortcut

from subsync import config, player, time
from subsync.time import Time
from subsync.gui.timemapper_ui import Ui_FormTimeMapper


Player = player.getplayer(config.playertype)


class FormTimeMapper(QDialog, Ui_FormTimeMapper):

    finished = pyqtSignal(list)

    def __init__(self, filetypes, filepaths, callback=None):
        super(FormTimeMapper, self).__init__()

        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.move(0, 0)
        self.ct_table.setRowCount(0)
        self.ct_table.setColumnCount(len(filepaths))
        self.ct_table.horizontalHeader().setResizeMode(
            QHeaderView.ResizeToContents)

        self.filetypes = filetypes
        self.filepaths = filepaths

        if callback is not None:
            self.finished.connect(callback)

        self.shortcuts = []

    def showEvent(self, event):
        self._add_shortcut(config.shortcut['timemapper_addpart'],
                           self.shortcut_addpart_activated)
        self._add_shortcut(config.shortcut['timemapper_addmap'],
                           self.shortcut_addmap_activated)
        self._add_shortcut(config.shortcut['timemapper_dellast'],
                           self.shortcut_dellast_activated)
        self._add_shortcut(config.shortcut['timemapper_finish'],
                           self.shortcut_finish_activated)
        self._add_shortcut(config.shortcut['timemapper_next'],
                           self.shortcut_next_activated)
        self._add_shortcut(config.shortcut['timemapper_next_with_time'],
                           self.shortcut_next_with_time_activated)

        self.players = [Player(x) for x in self.filepaths]
        self.players[0].activate()

    def closeEvent(self, event):

        self.activateWindow()

        self.shortcuts.clear()
        for p in self.players:
            p.close()

        self.timemap = []
        for j in range(self.ct_table.columnCount()):
            col = [self.ct_table.item(i, j).text()
                   for i in range(self.ct_table.rowCount())]
            col = [Time(x) if x != "" else None for x in col]
            self.timemap.append(col)
        self.finished.emit(self.timemap)

    def grabtimes(self, src_only=False):
        self.showinfo("正在获取时间...")
        try:
            times = []
            for type, player in zip(self.filetypes, self.players):
                if src_only and type != "src":
                    text = None
                else:
                    text = format(player.time, "srt")
                times.append(text)
        except Exception as ex:
            times = None
            logging.error("获取时间失败 {}".format(str(ex)))

        if times is not None:
            count = self.ct_table.rowCount()
            self.ct_table.setRowCount(count + 1)
            for i in range(len(self.players)):
                self.ct_table.setItem(count, i, QTableWidgetItem(times[i]))
            self.ct_table.setCurrentCell(count, 0, QItemSelectionModel.NoUpdate)
            self.ct_table.sortItems(0)
            self._color_list()
            self.showinfo("获取时间成功", type_='success')
        else:
            self.showinfo("获取时间失败", type_='error')

    def focus_next_player(self, with_time_sync=False):
        current_index = next((i for i in range(len(self.players))
            if self.players[i].is_active), len(self.players)-1)
        next_player = self.players[(current_index+1) % len(self.players)]
        next_player.activate()
        if with_time_sync:
            next_player.time = self.players[current_index].time

    def _get_times_by_row(self, row):
        texts = [self.ct_table.item(row, i).text()
                 for i in range(self.ct_table.columnCount())]
        times = [None if x == '' else Time(x) for x in texts]
        return times

    def _get_times_by_column(self, column):
        texts = [self.ct_table.item(i, column).text()
                 for i in range(self.ct_table.rowCount())]
        times = [None if x is None else Time(x) for x in texts]
        return times

    def _is_same_time_delta(self, times1, times2):
        # 所用项目非空（都是映射而不是分段）
        if all(times1) and all(times2):
            # 时间差在允许的范围内
            delta = [time1-time2 for time1, time2 in zip(times1, times2)]
            if time.is_approx_equal(min(delta), max(delta), Player.timedelta_tolerance):
                return True
        return False

    def _color_item(self, item, foreground, background):
        item.setForeground(QBrush(QColor(foreground)))
        item.setBackground(QBrush(QColor(background)))

    def _color_list(self):
        colors = cycle(config.timemapper_color)
        color = next(colors)

        row_count = self.ct_table.rowCount()
        column_count = self.ct_table.columnCount()

        times = [self._get_times_by_row(i) for i in range(row_count)]

        for i in range(row_count):
            if i > 0 and all(times[i-1]):
                if not self._is_same_time_delta(times[i], times[i-1]):
                    color = next(colors)
            for j in range(column_count):
                self._color_item(self.ct_table.item(i, j), *color)

    def _add_shortcut(self, key_sequence, slot):
        shortcut = QxtGlobalShortcut(QKeySequence(key_sequence))
        shortcut.activated.connect(slot)
        self.shortcuts.append(shortcut)

    def shortcut_addpart_activated(self):
        self.grabtimes(src_only=True)

    def shortcut_addmap_activated(self):
        self.grabtimes()

    def shortcut_dellast_activated(self):
        self.ct_table.removeRow(self.ct_table.rowCount() - 1)

    def shortcut_finish_activated(self):
        self.close()

    def shortcut_next_activated(self):
        self.focus_next_player()

    def shortcut_next_with_time_activated(self):
        self.focus_next_player(with_time_sync=True)

    def showinfo(self, s, type_='normal'):
        self.ct_info.setText(s)
        type_ = type_.lower()
        if type_ == 'normal':
            self.ct_info.setStyleSheet("")
        elif type_ == 'success':
            self.ct_info.setStyleSheet("color:green;")
        elif type_ == 'warning':
            self.ct_info.setStyleSheet("color:orange;")
        elif type_ == 'error':
            self.ct_info.setStyleSheet("color:red;")
        self.ct_info.repaint()
