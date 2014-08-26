# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timemapper.ui'
#
# Created: Wed Aug 27 01:47:02 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormTimeMapper(object):
    def setupUi(self, FormTimeMapper):
        FormTimeMapper.setObjectName("FormTimeMapper")
        FormTimeMapper.resize(200, 102)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormTimeMapper.sizePolicy().hasHeightForWidth())
        FormTimeMapper.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(FormTimeMapper)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setContentsMargins(2, 2, 2, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ct_table = QtWidgets.QTableWidget(FormTimeMapper)
        self.ct_table.setStyleSheet("font-family: monospace;")
        self.ct_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ct_table.setObjectName("ct_table")
        self.ct_table.setColumnCount(0)
        self.ct_table.setRowCount(0)
        self.ct_table.horizontalHeader().setVisible(False)
        self.ct_table.verticalHeader().setVisible(False)
        self.ct_table.verticalHeader().setDefaultSectionSize(20)
        self.verticalLayout.addWidget(self.ct_table)
        self.ct_info = QtWidgets.QLabel(FormTimeMapper)
        self.ct_info.setObjectName("ct_info")
        self.verticalLayout.addWidget(self.ct_info)

        self.retranslateUi(FormTimeMapper)
        QtCore.QMetaObject.connectSlotsByName(FormTimeMapper)

    def retranslateUi(self, FormTimeMapper):
        _translate = QtCore.QCoreApplication.translate
        FormTimeMapper.setWindowTitle(_translate("FormTimeMapper", "时间映射"))

