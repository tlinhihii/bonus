# Form implementation generated from reading ui file 'D:\Python\pycharm\KTLT\chap6\learnseaborn\bonus\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 49, 491, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 40, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButtonChoose = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonChoose.setGeometry(QtCore.QRect(30, 40, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonChoose.setFont(font)
        self.pushButtonChoose.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButtonChoose.setObjectName("pushButtonChoose")
        self.pushButtonOpen = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonOpen.setGeometry(QtCore.QRect(180, 110, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonOpen.setFont(font)
        self.pushButtonOpen.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButtonOpen.setObjectName("pushButtonOpen")
        self.pushButtonSave = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSave.setGeometry(QtCore.QRect(380, 110, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButtonSave.setObjectName("pushButtonSave")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "..."))
        self.pushButtonChoose.setText(_translate("MainWindow", "Choose File "))
        self.pushButtonOpen.setText(_translate("MainWindow", "Open Chart in Browser"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save Chart to HTML File"))
