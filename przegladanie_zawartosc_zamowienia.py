from PyQt5 import QtCore, QtGui, QtWidgets
from zawartosc_zamowienia import Ui_ViewOrdersContentWindow


class Ui_SearchOrderContentWindow(object):
    adress = None
    def openWindow(self):
        order_id = str(self.inputBox.toPlainText()).lower()
        sql = "SELECT * FROM zawartosc_zamowienia_view WHERE zamowienie_id= '" + str(order_id) + "'"
        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_ViewOrdersContentWindow()
            self.ui.setupUi(self.window, sql, self.adress)
            self.window.show()
        except:
            print("Błąd przy szukaniu cześci")
        pass


    def setupUi(self, SearchOrderContentWindow, adress):
        self.adress = adress
        SearchOrderContentWindow.setObjectName("SearchOrderContentWindow")
        SearchOrderContentWindow.resize(500, 410)
        self.centralwidget = QtWidgets.QWidget(SearchOrderContentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 460, 70))


        self.inputBox = QtWidgets.QTextEdit(self.centralwidget)
        self.inputBox.setGeometry((QtCore.QRect(20, 110, 460, 70)))
        txt = self.inputBox.toPlainText()


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(lambda: self.openWindow())
        self.pushButton.setGeometry(QtCore.QRect(20, 200, 460, 70))

        font = QtGui.QFont()
        font.setPointSize(16)
        self.inputBox.setFont(font)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        SearchOrderContentWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SearchOrderContentWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 21))
        self.menubar.setObjectName("menubar")
        SearchOrderContentWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SearchOrderContentWindow)
        self.statusbar.setObjectName("statusbar")
        SearchOrderContentWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SearchOrderContentWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchOrderContentWindow)

    def retranslateUi(self, SearchOrderContentWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchOrderContentWindow.setWindowTitle(_translate("SearchOrderContentWindow", "Przeglądanie zawartości zamówienia"))
        self.pushButton.setText(_translate("SearchOrderContentWindow", "Szukaj"))
        self.label.setText(_translate("SearchOrderContentWindow", "Wyszukaj zawartość zamówienia"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchOrderContentWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchOrderContentWindow()
    ui.setupUi(SearchOrderContentWindow, 1)
    SearchOrderContentWindow.show()
    sys.exit(app.exec_())