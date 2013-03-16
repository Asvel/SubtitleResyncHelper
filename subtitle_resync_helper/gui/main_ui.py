# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat Mar 16 17:50:20 2013
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
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.ct_tree_src = QtGui.QTreeWidget(self.scrollAreaWidgetContents)
        self.ct_tree_src.setMinimumSize(QtCore.QSize(0, 200))
        self.ct_tree_src.setStyleSheet(_fromUtf8("font-family: monospace;"))
        self.ct_tree_src.setObjectName(_fromUtf8("ct_tree_src"))
        item_0 = QtGui.QTreeWidgetItem(self.ct_tree_src)
        self.verticalLayout_3.addWidget(self.ct_tree_src)
        self.ct_tree_dst = QtGui.QTreeWidget(self.scrollAreaWidgetContents)
        self.ct_tree_dst.setMinimumSize(QtCore.QSize(0, 200))
        self.ct_tree_dst.setObjectName(_fromUtf8("ct_tree_dst"))
        self.verticalLayout_3.addWidget(self.ct_tree_dst)
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
        self.verticalLayout.setStretch(0, 1)
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
        QtCore.QObject.connect(self.ct_tree_src, QtCore.SIGNAL(_fromUtf8("itemClicked(QTreeWidgetItem*,int)")), MainWindow.ct_tree_src_clicked)
        QtCore.QObject.connect(self.ct_tree_src, QtCore.SIGNAL(_fromUtf8("itemExpanded(QTreeWidgetItem*)")), MainWindow.ct_tree_itemexpanded)
        QtCore.QObject.connect(self.ct_tree_src, QtCore.SIGNAL(_fromUtf8("collapsed(QModelIndex)")), MainWindow.ct_tree_itemcollapsed)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.scrollArea, self.ct_start)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.ct_tree_src.headerItem().setText(0, _translate("MainWindow", "原始文件", None))
        __sortingEnabled = self.ct_tree_src.isSortingEnabled()
        self.ct_tree_src.setSortingEnabled(False)
        self.ct_tree_src.topLevelItem(0).setText(0, _translate("MainWindow", "添加...", None))
        self.ct_tree_src.setSortingEnabled(__sortingEnabled)
        self.ct_tree_dst.headerItem().setText(0, _translate("MainWindow", "目标文件", None))
        self.ct_start.setText(_translate("MainWindow", "开始", None))

