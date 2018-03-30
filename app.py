__author__ = 'mittr'

from PyQt5 import QtCore, QtGui, QtWidgets
from urllib.request import urlopen as ureq
from PyQt5.QtWidgets import QTableWidgetItem
from bs4 import BeautifulSoup as Soup
import re
import operator
import urllib.request as urllib2


class Ui_MainWindow(object):

    def whey(self):
        # Let's fetch the soup for the page here!

        # Use this one for Whey Protein
        # my_url = 'https://www.amazon.in/Optimum-Nutrition-Standard-Protein-Powder/dp/B000QSNYGI/ref=sr_1_6?s=hpc&ie=UTF8&qid=1516012071&sr=1-6&keywords=whey+protein'

        # Use this for BCAA
        my_url = 'https://www.amazon.in/BSN-Amino-Servings-Green-Apple/dp/B0055BYEE2/ref=sr_1_17?s=hpc&ie=UTF8&qid=1522424648&sr=1-17&keywords=bcaa&th=1'

        uClient = ureq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = Soup(page_html, "html.parser")

        # A little bit of Regex here to fetch the list items with id's beginning with flavor_name_
        containers = page_soup.findAll("li", {"id": re.compile("^flavor_name_")})
        total = len(containers)

        # The solution set :)
        dictionary = {}
        i = 0
        for container in containers:
            print(container['title'][15:], '\t', container['data-dp-url'])
            while True:
                try:
                    if not container['data-dp-url']:
                        price = page_soup.find("span", {"id": "priceblock_ourprice"})
                        try:
                            print(type(price.text))
                            dictionary[str(container['title'][15:].strip())] = float(price.text.replace(u'\xa0', u' ').replace(',', '').strip())
                        except AttributeError as e:
                            print("Unavailable")
                            # dictionary[str(container['title'][15:].strip())] = 'Unavailable'
                        # now go to the link to fetch the price and store in the dictionary
                    else:
                        uCl = ureq('https://www.amazon.in/Optimum-Nutrition-Standard-Protein-Powder' + container['data-dp-url'])
                        html = uCl.read()
                        uCl.close()
                        soup = Soup(html, "html.parser")
                        price = soup.find("span", {"id": "priceblock_ourprice"})
                        try:
                            print(type(price.text))
                            # if type(price) != 'text':
                            #     price = page_soup.find("span", {"id": "a-color-price"})
                            dictionary[str(container['title'][15:].strip())] = float(price.text.replace(u'\xa0', u' ').replace(',', '').strip())
                        except AttributeError as e:
                            print("Unavailable")
                            # dictionary[str(container['title'][15:].strip())] = 'Unavailable'
                    i += 1
                    completed = (i/total)*100
                    self.progressBar.setValue(completed)
                    break
                except urllib2.HTTPError as err:
                    print("TRYING AGAIN - NETWORK ERROR")
        print("Flavors in non-descending order of price: \n")

        # Sorting the dictionary items in non decreasing order!
        sorted_x = sorted(dictionary.items(), key=operator.itemgetter(1))
        print(sorted_x)
        print(len(sorted_x))
        i = 0

        for flavor, price in sorted_x:
            self.tableWidget.setItem(i, 0, QTableWidgetItem(flavor))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(price)))
            print("{:<25} {:<7}".format(flavor, price))
            i += 1

    def handler(self):
        self.start.clicked.connect(self.whey)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Optimum Nutrition Minimum Price Finder @ Amazon India")
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
        self.tableWidget.setRowCount(17)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 321, 16))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 300, 241, 23))
        self.progressBar.setProperty("value", 0)
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
        self.centralwidget.setWindowIcon(QtGui.QIcon('favicon.png'))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Define custom handler
        self.handler()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("5LB Optimum Nutrition Minimum Price on Amazon India", "5LB Optimum Nutrition Minimum Price on Amazon India"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.size2.setText(_translate("MainWindow", "2 LB"))
        self.size5.setText(_translate("MainWindow", "5 LB"))
        self.size10.setText(_translate("MainWindow", "10 LB"))
        self.groupBox1.setTitle(_translate("MainWindow", ""))
        self.groupBox.setTitle(_translate("MainWindow", ""))
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
