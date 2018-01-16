# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mittr\Desktop\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(80, 130, 100, 30))
        self.start.setMaximumSize(QtCore.QSize(100, 30))
        self.start.setObjectName("start")
        self.size2 = QtWidgets.QRadioButton(self.centralwidget)
        self.size2.setGeometry(QtCore.QRect(40, 70, 61, 17))
        self.size2.setCheckable(False)
        self.size2.setObjectName("size2")
        self.size5 = QtWidgets.QRadioButton(self.centralwidget)
        self.size5.setGeometry(QtCore.QRect(110, 70, 82, 17))
        self.size5.setChecked(True)
        self.size5.setObjectName("size5")
        self.size10 = QtWidgets.QRadioButton(self.centralwidget)
        self.size10.setGeometry(QtCore.QRect(180, 70, 82, 17))
        self.size10.setCheckable(False)
        self.size10.setObjectName("size10")
        self.groupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox1.setGeometry(QtCore.QRect(20, 50, 231, 151))
        self.groupBox1.setObjectName("groupBox1")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(280, 30, 301, 331))
        self.groupBox.setObjectName("groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 271, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 321, 16))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 300, 241, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.groupBox1.raise_()
        self.groupBox.raise_()
        self.label.raise_()
        self.progressBar.raise_()
        self.size10.raise_()
        self.size2.raise_()
        self.start.raise_()
        self.size5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.size2.setText(_translate("MainWindow", "2 LB"))
        self.size5.setText(_translate("MainWindow", "5 LB"))
        self.size10.setText(_translate("MainWindow", "10 LB"))
        self.groupBox1.setTitle(_translate("MainWindow", "GroupBox"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Flavor"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price"))
        self.label.setText(_translate("MainWindow", "Find the minimum priced ON Whey Protein Flavor on Amazon.in!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

