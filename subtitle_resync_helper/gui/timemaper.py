# -*- coding: utf-8 -*-

import logging

from PyQt4.QtCore import Qt, pyqtSignal
from PyQt4.QtGui import (QDialog, QKeySequence, QApplication,
                         QTableWidgetItem, QHeaderView, QMessageBox)
from pygs import QxtGlobalShortcut

from subtitle_resync_helper import config, player, time
from subtitle_resync_helper.gui.timemaper_ui import Ui_FormTimeMapper


Player = player.getplayer(config.playername)

class FormTimeMapper(QDialog, Ui_FormTimeMapper):

    finished = pyqtSignal(list)

    def __init__(self, filetypes, filepaths, callback=None):
        super(FormTimeMapper, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.move(0, 0)

        self.filetypes = filetypes
        self.filepaths = filepaths
        if callback is not None:
            self.finished.connect(callback)

        self.shortcuts = []

        self.ct_table.setRowCount(0)
        self.ct_table.setColumnCount(len(self.filepaths))
        self.ct_table.horizontalHeader().setResizeMode(
            QHeaderView.ResizeToContents)

    def _get_texts_by_row(self, row):
        return [self.ct_table.item(row, i).text()
                for i in range(self.ct_table.columnCount())]

    def _get_texts_by_column(self, column):
        return [self.ct_table.item(i, column).text()
                for i in range(self.ct_table.rowCount())]

    def showEvent(self, event):
        self.add_shortcut(config.shortcut['timemaper_addpart'],
                          self.shortcut_addpart_activated)
        self.add_shortcut(config.shortcut['timemaper_addmap'],
                          self.shortcut_addmap_activated)
        self.add_shortcut(config.shortcut['timemaper_dellast'],
                          self.shortcut_dellast_activated)
        self.add_shortcut(config.shortcut['timemaper_finish'],
                          self.shortcut_finish_activated)
        self.add_shortcut(config.shortcut['timemaper_next'],
                          self.shortcut_next_activated)
        self.add_shortcut(config.shortcut['timemaper_next_with_time'],
                          self.shortcut_next_with_time_activated)

        self.players = [Player(x) for x in self.filepaths]
        self.players[0].activate()

    def closeEvent(self, event):

        self.activateWindow()

        # 结尾校验
        endcheck = self._is_same_time_delta(-1, -2)
        if not endcheck:
            result = QMessageBox.warning(self, "警告",
            "结尾校验没用通过，可能遗漏了时间映射，是否继续？",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if result != QMessageBox.Yes:
                event.ignore()
                return

        self.shortcuts.clear()
        for p in self.players:
            p.close()

        self.timemap = []
        for j in range(self.ct_table.columnCount()):
            col = [self.ct_table.item(i, j).text()
                   for i in range(self.ct_table.rowCount())]
            col = [time.parse(x) if x != "" else None for x in col]
            self.timemap.append(col)
        if endcheck:
            for tm in self.timemap:
                del tm[len(tm) - 1]
        self.finished.emit(self.timemap)

    def grabtimes(self, src_only=False):
        self.showinfo("正在获取时间...")
        try:
            times = []
            for type, player in zip(self.filetypes, self.players):
                if src_only and type != "src":
                    text = None
                else:
                    text = str(player.time)
                times.append(text)
        except Exception as ex:
            times = None
            logging.error("获取时间失败 {}".format(str(ex)))
        if times is not None:
            count = self.ct_table.rowCount()
            self.ct_table.setRowCount(count + 1)
            for i in range(len(self.players)):
                self.ct_table.setItem(count, i, QTableWidgetItem(times[i]))
            self.ct_table.setCurrentCell(count, 0)
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

    def _is_same_time_delta(self, row_index_1, row_index_2):
        count = self.ct_table.rowCount()
        if row_index_1 < 0:
            row_index_1 += count
        if row_index_2 < 0:
            row_index_2 += count

        # 行号存在
        if not (0 <= row_index_1 < count and 0 <= row_index_2 < count):
            return False

        texts1 = self._get_texts_by_row(row_index_1)
        texts2 = self._get_texts_by_row(row_index_2)

        # 所用项目非空（都是映射而不是分段）
        if not (all(texts1) and all(texts2)):
            return False

        # 时间都能正常解析
        try:
            times1 = [time.parse(x) for x in texts1]
            times2 = [time.parse(x) for x in texts2]
        except:
            return False

        # 时间差在允许的范围内
        delta = [time1-time2 for time1,time2 in zip(times1,times2)]
        if not time.is_approx_equal(min(delta), max(delta)):
            return False

        return True

    def add_shortcut(self, key_sequence, slot):
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
        self.focus_next_player(True)

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
