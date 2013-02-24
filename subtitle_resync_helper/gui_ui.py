# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sun Feb 24 20:50:07 2013
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
        Form.resize(400, 300)
        self.ct_switch = QtGui.QPushButton(Form)
        self.ct_switch.setGeometry(QtCore.QRect(10, 210, 251, 23))
        self.ct_switch.setObjectName(_fromUtf8("ct_switch"))
        self.ct_list = QtGui.QListWidget(Form)
        self.ct_list.setGeometry(QtCore.QRect(10, 10, 251, 192))
        self.ct_list.setObjectName(_fromUtf8("ct_list"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.ct_switch, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.ct_switch_clicked)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.ct_switch.setText(_translate("Form", "开始", None))

