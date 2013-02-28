# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\project\SubtitleResyncHelper\subtitle_resync_helper\gui.ui'
#
# Created: Thu Feb 28 13:01:26 2013
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
        Form.resize(400, 200)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ct_switch = QtGui.QPushButton(Form)
        self.ct_switch.setObjectName(_fromUtf8("ct_switch"))
        self.gridLayout.addWidget(self.ct_switch, 1, 0, 1, 1)
        self.ct_table = QtGui.QTableWidget(Form)
        self.ct_table.setObjectName(_fromUtf8("ct_table"))
        self.ct_table.setColumnCount(0)
        self.ct_table.setRowCount(0)
        self.ct_table.verticalHeader().setVisible(False)
        self.ct_table.verticalHeader().setDefaultSectionSize(20)
        self.gridLayout.addWidget(self.ct_table, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.ct_switch, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.ct_switch_clicked)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.ct_switch.setText(_translate("Form", "开始", None))

