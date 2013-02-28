# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\project\SubtitleResyncHelper\subtitle_resync_helper\gui.ui'
#
# Created: Thu Feb 28 18:30:06 2013
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
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ct_table = QtGui.QTableWidget(Form)
        self.ct_table.setStyleSheet(_fromUtf8("font-family: monospace;"))
        self.ct_table.setObjectName(_fromUtf8("ct_table"))
        self.ct_table.setColumnCount(0)
        self.ct_table.setRowCount(0)
        self.ct_table.horizontalHeader().setVisible(False)
        self.ct_table.verticalHeader().setVisible(False)
        self.ct_table.verticalHeader().setDefaultSectionSize(20)
        self.verticalLayout.addWidget(self.ct_table)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.ct_info = QtGui.QLabel(Form)
        self.ct_info.setObjectName(_fromUtf8("ct_info"))
        self.horizontalLayout_3.addWidget(self.ct_info)
        self.ct_switch = QtGui.QPushButton(Form)
        self.ct_switch.setObjectName(_fromUtf8("ct_switch"))
        self.horizontalLayout_3.addWidget(self.ct_switch)
        self.horizontalLayout_3.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.ct_switch, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.ct_switch_clicked)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", " ", None))
        self.ct_switch.setText(_translate("Form", "开始", None))

