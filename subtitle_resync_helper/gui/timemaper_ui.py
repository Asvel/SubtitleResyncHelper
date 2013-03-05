# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/timemaper.ui'
#
# Created: Tue Mar  5 12:43:47 2013
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(160, 102)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setContentsMargins(2, 2, 2, 3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ct_table = QtGui.QTableWidget(Form)
        self.ct_table.setStyleSheet(_fromUtf8("font-family: monospace;"))
        self.ct_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.ct_table.setObjectName(_fromUtf8("ct_table"))
        self.ct_table.setColumnCount(0)
        self.ct_table.setRowCount(0)
        self.ct_table.horizontalHeader().setVisible(False)
        self.ct_table.verticalHeader().setVisible(False)
        self.ct_table.verticalHeader().setDefaultSectionSize(20)
        self.verticalLayout.addWidget(self.ct_table)
        self.ct_info = QtGui.QLabel(Form)
        self.ct_info.setObjectName(_fromUtf8("ct_info"))
        self.verticalLayout.addWidget(self.ct_info)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", " ", None))

