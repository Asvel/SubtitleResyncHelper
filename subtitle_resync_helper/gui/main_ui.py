# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat Apr 20 21:54:59 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet(_fromUtf8(""))
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 782, 510))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.ct_layout_0 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.ct_layout_0.setMargin(0)
        self.ct_layout_0.setObjectName(_fromUtf8("ct_layout_0"))
        self.ct_groupbox_src = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.ct_groupbox_src.setObjectName(_fromUtf8("ct_groupbox_src"))
        self.ct_layout_dst_1 = QtGui.QHBoxLayout(self.ct_groupbox_src)
        self.ct_layout_dst_1.setSpacing(2)
        self.ct_layout_dst_1.setContentsMargins(6, 2, 6, 6)
        self.ct_layout_dst_1.setObjectName(_fromUtf8("ct_layout_dst_1"))
        self.ct_tree_src = QtGui.QTreeWidget(self.ct_groupbox_src)
        self.ct_tree_src.setMinimumSize(QtCore.QSize(0, 200))
        self.ct_tree_src.setStyleSheet(_fromUtf8("font-family: monospace;"))
        self.ct_tree_src.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.ct_tree_src.setObjectName(_fromUtf8("ct_tree_src"))
        self.ct_tree_src.header().setVisible(False)
        self.ct_layout_dst_1.addWidget(self.ct_tree_src)
        self.ct_layout_dst_2 = QtGui.QVBoxLayout()
        self.ct_layout_dst_2.setSpacing(2)
        self.ct_layout_dst_2.setObjectName(_fromUtf8("ct_layout_dst_2"))
        self.ct_append_src = QtGui.QPushButton(self.ct_groupbox_src)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ct_append_src.sizePolicy().hasHeightForWidth())
        self.ct_append_src.setSizePolicy(sizePolicy)
        self.ct_append_src.setObjectName(_fromUtf8("ct_append_src"))
        self.ct_layout_dst_2.addWidget(self.ct_append_src)
        self.ct_remove_src = QtGui.QPushButton(self.ct_groupbox_src)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ct_remove_src.sizePolicy().hasHeightForWidth())
        self.ct_remove_src.setSizePolicy(sizePolicy)
        self.ct_remove_src.setObjectName(_fromUtf8("ct_remove_src"))
        self.ct_layout_dst_2.addWidget(self.ct_remove_src)
        self.ct_clear_src = QtGui.QPushButton(self.ct_groupbox_src)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ct_clear_src.sizePolicy().hasHeightForWidth())
        self.ct_clear_src.setSizePolicy(sizePolicy)
        self.ct_clear_src.setObjectName(_fromUtf8("ct_clear_src"))
        self.ct_layout_dst_2.addWidget(self.ct_clear_src)
        self.ct_clean_src = QtGui.QPushButton(self.ct_groupbox_src)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ct_clean_src.sizePolicy().hasHeightForWidth())
        self.ct_clean_src.setSizePolicy(sizePolicy)
        self.ct_clean_src.setObjectName(_fromUtf8("ct_clean_src"))
        self.ct_layout_dst_2.addWidget(self.ct_clean_src)
        self.ct_layout_dst_1.addLayout(self.ct_layout_dst_2)
        self.ct_layout_0.addWidget(self.ct_groupbox_src)
        self.ct_groupbox_dst = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.ct_groupbox_dst.setObjectName(_fromUtf8("ct_groupbox_dst"))
        self.ct_layout_src_1 = QtGui.QHBoxLayout(self.ct_groupbox_dst)
        self.ct_layout_src_1.setSpacing(2)
        self.ct_layout_src_1.setContentsMargins(6, 2, 6, 6)
        self.ct_layout_src_1.setObjectName(_fromUtf8("ct_layout_src_1"))
        self.ct_tree_dst = QtGui.QTreeWidget(self.ct_groupbox_dst)
        self.ct_tree_dst.setMinimumSize(QtCore.QSize(0, 200))
        self.ct_tree_dst.setStyleSheet(_fromUtf8("font-family: monospace;"))
        self.ct_tree_dst.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.ct_tree_dst.setObjectName(_fromUtf8("ct_tree_dst"))
        self.ct_tree_dst.header().setVisible(False)
        self.ct_layout_src_1.addWidget(self.ct_tree_dst)
        self.ct_layout_src_2 = QtGui.QVBoxLayout()
        self.ct_layout_src_2.setSpacing(2)
        self.ct_layout_src_2.setObjectName(_fromUtf8("ct_layout_src_2"))
        self.ct_append_dst = QtGui.QPushButton(self.ct_groupbox_dst)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ct_append_dst.sizePolicy().hasHeightForWidth())
        self.ct_append_dst.setSizePolicy(sizePolicy)
        self.ct_append_dst.setObjectName(_fromUtf8("ct_append_dst"))
        self.ct_layout_src_2.addWidget(self.ct_append_dst)
        self.ct_remove_dst = QtGui.QPushButton(self.ct_groupbox_dst)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ct_remove_dst.sizePolicy().hasHeightForWidth())
        self.ct_remove_dst.setSizePolicy(sizePolicy)
        self.ct_remove_dst.setObjectName(_fromUtf8("ct_remove_dst"))
        self.ct_layout_src_2.addWidget(self.ct_remove_dst)
        self.ct_clear_dst = QtGui.QPushButton(self.ct_groupbox_dst)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ct_clear_dst.sizePolicy().hasHeightForWidth())
        self.ct_clear_dst.setSizePolicy(sizePolicy)
        self.ct_clear_dst.setObjectName(_fromUtf8("ct_clear_dst"))
        self.ct_layout_src_2.addWidget(self.ct_clear_dst)
        self.ct_clean_dst = QtGui.QPushButton(self.ct_groupbox_dst)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ct_clean_dst.sizePolicy().hasHeightForWidth())
        self.ct_clean_dst.setSizePolicy(sizePolicy)
        self.ct_clean_dst.setObjectName(_fromUtf8("ct_clean_dst"))
        self.ct_layout_src_2.addWidget(self.ct_clean_dst)
        self.ct_layout_src_1.addLayout(self.ct_layout_src_2)
        self.ct_layout_0.addWidget(self.ct_groupbox_dst)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ct_start = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ct_start.sizePolicy().hasHeightForWidth())
        self.ct_start.setSizePolicy(sizePolicy)
        self.ct_start.setObjectName(_fromUtf8("ct_start"))
        self.horizontalLayout.addWidget(self.ct_start)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.ct_start, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.ct_start_clicked)
        QtCore.QObject.connect(self.ct_tree_src, QtCore.SIGNAL(_fromUtf8("itemCollapsed(QTreeWidgetItem*)")), MainWindow.ct_tree_itemcollapsed)
        QtCore.QObject.connect(self.ct_append_src, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.ct_append_src_clicked)
        QtCore.QObject.connect(self.ct_remove_src, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.ct_remove_clicked)
        QtCore.QObject.connect(self.ct_clean_src, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.ct_clean_src_clicked)
        QtCore.QObject.connect(self.ct_append_dst, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.ct_append_dst_clicked)
        QtCore.QObject.connect(self.ct_remove_dst, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.ct_remove_clicked)
        QtCore.QObject.connect(self.ct_clean_dst, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.ct_clean_dst_clicked)
        QtCore.QObject.connect(self.ct_tree_src, QtCore.SIGNAL(_fromUtf8("itemExpanded(QTreeWidgetItem*)")), MainWindow.ct_tree_itemexpanded)
        QtCore.QObject.connect(self.ct_clear_src, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.ct_clear_clicked)
        QtCore.QObject.connect(self.ct_clear_dst, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.ct_clear_clicked)
        QtCore.QObject.connect(self.ct_tree_dst, QtCore.SIGNAL(_fromUtf8("itemCollapsed(QTreeWidgetItem*)")), MainWindow.ct_tree_itemcollapsed)
        QtCore.QObject.connect(self.ct_tree_dst, QtCore.SIGNAL(_fromUtf8("itemExpanded(QTreeWidgetItem*)")), MainWindow.ct_tree_itemexpanded)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.scrollArea, self.ct_tree_src)
        MainWindow.setTabOrder(self.ct_tree_src, self.ct_append_src)
        MainWindow.setTabOrder(self.ct_append_src, self.ct_remove_src)
        MainWindow.setTabOrder(self.ct_remove_src, self.ct_clean_src)
        MainWindow.setTabOrder(self.ct_clean_src, self.ct_tree_dst)
        MainWindow.setTabOrder(self.ct_tree_dst, self.ct_append_dst)
        MainWindow.setTabOrder(self.ct_append_dst, self.ct_remove_dst)
        MainWindow.setTabOrder(self.ct_remove_dst, self.ct_clean_dst)
        MainWindow.setTabOrder(self.ct_clean_dst, self.ct_start)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SubtitleResyncHelper", None))
        self.ct_groupbox_src.setTitle(_translate("MainWindow", "原始文件", None))
        self.ct_tree_src.headerItem().setText(0, _translate("MainWindow", "name", None))
        self.ct_tree_src.headerItem().setText(1, _translate("MainWindow", "dir", None))
        self.ct_append_src.setText(_translate("MainWindow", "添加", None))
        self.ct_remove_src.setText(_translate("MainWindow", "移除", None))
        self.ct_clear_src.setText(_translate("MainWindow", "清空", None))
        self.ct_clean_src.setText(_translate("MainWindow", "清理", None))
        self.ct_groupbox_dst.setTitle(_translate("MainWindow", "目标文件", None))
        self.ct_tree_dst.headerItem().setText(0, _translate("MainWindow", "name", None))
        self.ct_tree_dst.headerItem().setText(1, _translate("MainWindow", "dir", None))
        self.ct_append_dst.setText(_translate("MainWindow", "添加", None))
        self.ct_remove_dst.setText(_translate("MainWindow", "移除", None))
        self.ct_clear_dst.setText(_translate("MainWindow", "清空", None))
        self.ct_clean_dst.setText(_translate("MainWindow", "清理", None))
        self.ct_start.setText(_translate("MainWindow", "开始", None))

