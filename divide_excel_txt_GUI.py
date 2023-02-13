# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import os
import pandas as pd


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(747, 646)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.lineEdit_file_path = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_file_path.setGeometry(QtCore.QRect(140, 90, 451, 31))
        self.lineEdit_file_path.setReadOnly(True)
        self.lineEdit_file_path.setObjectName("lineEdit_file_path")
        self.pushButton_Load_QR = QtWidgets.QPushButton(Dialog)
        self.pushButton_Load_QR.setGeometry(QtCore.QRect(600, 90, 111, 31))
        self.pushButton_Load_QR.setObjectName("pushButton_Load_QR")
        self.pushButton_Load_QR.clicked.connect(self.OnClickFindQR)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 90, 61, 31))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(80, 160, 121, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_rename_file = QtWidgets.QLabel(Dialog)
        self.label_rename_file.setGeometry(QtCore.QRect(80, 140, 81, 21))
        self.label_rename_file.setObjectName("label_rename_file")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(330, 160, 151, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_txt_divide = QtWidgets.QLabel(Dialog)
        self.label_txt_divide.setGeometry(QtCore.QRect(330, 140, 141, 21))
        self.label_txt_divide.setObjectName("label_txt_divide")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(40, 210, 671, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pushButton_devide_text = QtWidgets.QPushButton(Dialog)
        self.pushButton_devide_text.setGeometry(QtCore.QRect(600, 150, 111, 31))
        self.pushButton_devide_text.setObjectName("pushButton_devide_text")
        self.pushButton_devide_text.clicked.connect(self.OnClickDivideQR)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_Load_QR.setText(_translate("Dialog", "QR 코드 불러오기"))
        self.label.setText(_translate("Dialog", "QR 코드 "))
        self.label_rename_file.setText(_translate("Dialog", "파일명 변경"))
        self.label_txt_divide.setText(_translate("Dialog", "텍스트 나누기를 할 기호"))
        self.pushButton_devide_text.setText(_translate("Dialog", "텍스트 나누기"))

    def OnClickFindQR(self):
        self.dir_path = QtWidgets.QFileDialog.getOpenFileName(Dialog ,'Find QR')
        self.lineEdit_file_path.setText(self.dir_path[0])
        if self.dir_path[0]:
            self.file_open = pd.read_excel(self.dir_path[0])

    def OnClickDivideQR(self):
        txt = self.textEdit_2.toPlainText()
        file_open = pd.read_excel(self.dir_path[0], sheet_name= 0, header = None)
        split_file = file_open[0].str.split(txt, expand=True)
        first_remove = split_file[~split_file[0].str.contains("[ㄱ-ㅣ가-힣]+", na=True, case=False)]
        second_remove = first_remove[~first_remove[2].str.contains("[ㄱ-ㅣ가-힣]+", na=True, case=False)]
        self.sort_file = second_remove.sort_values(by=[3,0], ascending=[True, True])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())