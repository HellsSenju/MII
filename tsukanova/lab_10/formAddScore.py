# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormAddScores.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QListView, QMessageBox
from Model import Model
from typing import List


class Ui_MainWindow(object):
    def __init__(self, scores: List[Model]):
        self.kol = 1
        self.scores: List[Model] = scores

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 462)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 181, 441, 181))
        self.listWidget.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(120, 50, 331, 31))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 100, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 100, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_a = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_a.setGeometry(QtCore.QRect(30, 100, 101, 20))
        self.lineEdit_a.setObjectName("lineEdit_a")
        self.lineEdit_b = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_b.setGeometry(QtCore.QRect(190, 100, 101, 20))
        self.lineEdit_b.setObjectName("lineEdit_b")
        self.lineEdit_c = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_c.setGeometry(QtCore.QRect(350, 100, 101, 20))
        self.lineEdit_c.setObjectName("lineEdit_c")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(10, 140, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet("background-color: rgb(182, 241, 143); border: none;")
        self.pushButton_add.setObjectName("pushButton_add")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_del = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_del.setGeometry(QtCore.QRect(10, 380, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_del.setFont(font)
        self.pushButton_del.setStyleSheet("background-color: rgb(255, 101, 103); border: none;")
        self.pushButton_del.setObjectName("pushButton_del")
        self.pushButton_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_confirm.setGeometry(QtCore.QRect(10, 420, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_confirm.setFont(font)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # мое
        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Название:"))
        self.label_2.setText(_translate("MainWindow", "a:"))
        self.label_3.setText(_translate("MainWindow", "b:"))
        self.label_4.setText(_translate("MainWindow", "c:"))
        self.pushButton_add.setText(_translate("MainWindow", "Добавить"))
        self.label_5.setText(_translate("MainWindow", "Добавление оценок"))
        self.pushButton_del.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_confirm.setText(_translate("MainWindow", "Подтвердить оценки"))

        # задание значений по умолчанию
        self.lineEdit_name.setText("Оценка_" + str(self.kol))
        self.lineEdit_a.setText("5")
        self.lineEdit_b.setText("10")
        self.lineEdit_c.setText("15")

    def add_functions(self):
        self.pushButton_add.clicked.connect(self.add_score)
        self.pushButton_del.clicked.connect(self.del_score)

    def add_score(self):
        self.scores.append(Model(self.lineEdit_name.text(),
                                 int(self.lineEdit_a.text()),
                                 int(self.lineEdit_b.text()),
                                 int(self.lineEdit_c.text())
                                 ))
        self.listWidget.addItem(
            f'{self.lineEdit_name.text()} a={self.lineEdit_a.text()}, b={self.lineEdit_b.text()}, c={self.lineEdit_c.text()}')

    def del_score(self):
        item = self.listWidget.currentItem().text().split()[0]
        self.scores.remove([i for i in self.scores if i.name == item][0])
        self.update_list_widget()

    def update_list_widget(self):
        self.listWidget.clear()
        for item in self.scores:
            self.listWidget.addItem(f'{item.name} a={item.a}, b={item.b}, c={item.c}')
