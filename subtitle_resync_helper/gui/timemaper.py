# -*- coding: utf-8 -*-

from PyQt4.QtCore import Qt, pyqtSignal
from PyQt4.QtGui import (QDialog, QKeySequence, QApplication,
                         QTableWidgetItem, QHeaderView)
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

        self.ct_table.setRowCount(0)
        self.ct_table.setColumnCount(len(self.filepaths))
        self.ct_table.horizontalHeader().setResizeMode(
            QHeaderView.ResizeToContents)

        self.showinfo("F5获取映射 F4获取分段")

    def showEvent(self, event):
        self.shortcut_addpart = QxtGlobalShortcut(QKeySequence("F4"))
        self.shortcut_addpart.activated.connect(self.shortcut_addpart_activated)
        self.shortcut_addmap = QxtGlobalShortcut(QKeySequence("F5"))
        self.shortcut_addmap.activated.connect(self.shortcut_addmap_activated)
        self.shortcut_dellast = QxtGlobalShortcut(QKeySequence("F9"))
        self.shortcut_dellast.activated.connect(self.shortcut_dellast_activated)
        self.shortcut_finish = QxtGlobalShortcut(QKeySequence("F11"))
        self.shortcut_finish.activated.connect(self.shortcut_finish_activated)

        self.players = [Player(x) for x in self.filepaths]

    def closeEvent(self, event):
        event.accept()

        del self.shortcut_addpart
        del self.shortcut_addmap
        del self.shortcut_dellast
        del self.shortcut_finish
        for p in self.players:
            p.close()

        self.timemap = []
        for j in range(self.ct_table.columnCount()):
            self.timemap.append([time.parse(self.ct_table.item(i, j).text())
                          for i in range(self.ct_table.rowCount())])
        self.finished.emit(self.timemap)

    def grabtimes(self, src_only=False):
        self.showinfo("正在获取时间...")
        try:
            times = []
            for type, player in zip(self.filetypes, self.players):
                if src_only and type != "src":
                    text = None
                else:
                    text = str(player.grabtime())
                times.append(text)
        except Exception:
            times = None
        if times is not None:
            count = self.ct_table.rowCount()
            self.ct_table.setRowCount(count + 1)
            for i in range(len(self.players)):
                self.ct_table.setItem(count, i, QTableWidgetItem(times[i]))
            self.ct_table.setCurrentCell(count, 0)
            self.showinfo("获取时间成功", type_='success')
        else:
            self.showinfo("获取时间失败", type_='error')

    def shortcut_addpart_activated(self):
        self.grabtimes(src_only=True)

    def shortcut_addmap_activated(self):
        self.grabtimes()

    def shortcut_dellast_activated(self):
        self.ct_table.removeRow(self.ct_table.rowCount() - 1)

    def shortcut_finish_activated(self):
        self.close()

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
