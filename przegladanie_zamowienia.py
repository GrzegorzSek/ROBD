from PyQt5 import QtCore, QtGui, QtWidgets
from zamowienia import Ui_ViewOrdersWindow


class Ui_SearchOrderWindow(object):
    adress = None
    def openWindow(self):
        client_id = str(self.inputBox.toPlainText()).lower()
        sql = "SELECT * FROM zamowienie_view WHERE klient_id='" + int(client_id) + "'"
        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_ViewOrdersWindow()
            self.ui.setupUi(self.window, sql, self.adress)
            self.window.show()
        except:
            print("Błąd przy szukaniu cześci")
        pass


    def setupUi(self, SearchOrderWindow, adress):
        self.adress = adress
        SearchOrderWindow.setObjectName("SearchOrderWindow")
        SearchOrderWindow.resize(500, 410)
        self.centralwidget = QtWidgets.QWidget(SearchOrderWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 460, 70))

        # self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        # self.comboBox.setGeometry(QtCore.QRect(20, 110, 460, 70))
        # self.comboBox.setObjectName("comboBox")
        # self.comboBox.addItem("Nazwa")
        # self.comboBox.addItem("Model")

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
        SearchOrderWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SearchOrderWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 21))
        self.menubar.setObjectName("menubar")
        SearchOrderWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SearchOrderWindow)
        self.statusbar.setObjectName("statusbar")
        SearchOrderWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SearchOrderWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchOrderWindow)

    def retranslateUi(self, SearchOrderWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchOrderWindow.setWindowTitle(_translate("SearchOrderWindow", "Przeglądanie zamówień"))
        self.pushButton.setText(_translate("SearchOrderWindow", "Szukaj"))
        self.label.setText(_translate("SearchOrderWindow", "Wyszukaj klienta"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchOrderWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchOrderWindow()
    ui.setupUi(SearchOrderWindow, 1)
    SearchOrderWindow.show()
    sys.exit(app.exec_())