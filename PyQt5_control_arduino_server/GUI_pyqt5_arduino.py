# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_pyqt5_arduino.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from arduino_control_firmat_20190413 import server_run
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(100, 240, 251, 181))
        self.dial.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.dial.setMinimum(544)
        self.dial.setMaximum(2400)
        self.dial.setObjectName("dial")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(430, 280, 171, 101))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 200, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 230, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(430, 150, 241, 41))
        self.progressBar.setMinimum(544)
        self.progressBar.setMaximum(2400)
        self.progressBar.setProperty("value", 543)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 100, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 20, 511, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.dial.sliderMoved['int'].connect(self.lcdNumber.display)
        self.dial.sliderMoved['int'].connect(self.progressBar.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        """
        connect pushbutten to print function or other function !
        # when you want to connect to another function ,the function must has bo ()
        for example function() is wrong , you must write like function !!
        """
        # self.pushButton.clicked.connect(self.connect_function)

        self.dial.sliderMoved['int'].connect(self.connect_function)

    def connect_function(self):
        print(self.lcdNumber.value())
        server_run(self.lcdNumber.value())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "slide this QDial "))
        self.label_2.setText(_translate("MainWindow", "number of degree"))
        self.label_3.setText(_translate("MainWindow", "percentage of degree"))
        self.label_4.setText(_translate("MainWindow", "This is Demo which show how Pyqt5 control arduino servo motor"))

