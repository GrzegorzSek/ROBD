from PyQt5 import QtCore, QtGui, QtWidgets
from szukanie_czesci_part1 import  Ui_SearchPartWindow
from dodawanie_czesci_part1 import Ui_AddPartWindow
from przegladanie_czesci import Ui_ViewPartsWindow
from przegladanie_klienci import Ui_ViewClientsWindow
from przegladanie_auta import Ui_ViewCarsWindow



class Ui_SecondSetupWindow(object):

    adress = 'c##scott/tiger@//192.168.0.8:1521/orcl1'

    def openWindow(self, number):
        if number == 1:
            try:
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_AddPartWindow()
                self.ui.setupUi(self.window, self.adress)
                self.window.show()
            except:
                print("Błąd")
        elif number == 2:
            try:
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_SearchPartWindow()
                self.ui.setupUi(self.window, self.adress)
                self.window.show()
            except:
                print("Błąd")
        elif number == 3:
            try:
                sql_code = """SELECT * FROM czesc_view"""
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_ViewPartsWindow()
                self.ui.setupUi(self.window, sql_code, self.adress)
                self.window.show()
            except:
                print("Błąd")
        elif number == 4:
            try:
                sql_code = """SELECT * FROM klient_view"""
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_ViewClientsWindow()
                self.ui.setupUi(self.window, sql_code, self.adress)
                self.window.show()
            except:
                print("Błąd")
        else:
            try:
                sql_code = """SELECT * FROM auta_view"""
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_ViewCarsWindow()
                self.ui.setupUi(self.window, sql_code, self.adress)
                self.window.show()
            except:
                print("Błąd")

    def setupUi(self, SecondSetupWindow):
        SecondSetupWindow.setObjectName("SecondSetupWindow")
        SecondSetupWindow.resize(750, 500)
        self.centralwidget = QtWidgets.QWidget(SecondSetupWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.dodajczesc = QtWidgets.QPushButton(self.centralwidget)
        self.dodajczesc.clicked.connect(lambda: self.openWindow(1))
        self.dodajczesc.setGeometry(QtCore.QRect(20, 20, 215, 70))

        self.znajdzczesc = QtWidgets.QPushButton(self.centralwidget)
        self.znajdzczesc.clicked.connect(lambda: self.openWindow(2))
        self.znajdzczesc.setGeometry(QtCore.QRect(20, 110, 215, 70))

        self.przegladajczesci = QtWidgets.QPushButton(self.centralwidget)
        self.przegladajczesci.clicked.connect(lambda: self.openWindow(3))
        self.przegladajczesci.setGeometry(QtCore.QRect(20, 200, 215, 70))

        self.znajdzklienci = QtWidgets.QPushButton(self.centralwidget)
        self.znajdzklienci.clicked.connect(lambda: self.openWindow(4))
        self.znajdzklienci.setGeometry(QtCore.QRect(20, 290, 215, 70))

        self.przegladajauto = QtWidgets.QPushButton(self.centralwidget)
        self.przegladajauto.clicked.connect(lambda: self.openWindow(5))
        self.przegladajauto.setGeometry(QtCore.QRect(20, 380, 215, 70))

        font = QtGui.QFont()
        font.setPointSize(17)
        self.przegladajauto.setFont(font)
        self.przegladajauto.setObjectName("przegladajauto")

        self.dodajczesc.setFont(font)
        self.dodajczesc.setObjectName("dodajczesc")

        self.znajdzczesc.setFont(font)
        self.znajdzczesc.setObjectName("znajdzczesc")

        self.znajdzklienci.setFont(font)
        self.znajdzklienci.setObjectName("znajdzklienci")

        self.przegladajczesci.setFont(font)
        self.przegladajczesci.setObjectName("przegladajczesci")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(250, 80, 455, 338))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("logo.png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")


        SecondSetupWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondSetupWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 20))
        self.menubar.setObjectName("menubar")
        SecondSetupWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondSetupWindow)
        self.statusbar.setObjectName("statusbar")
        SecondSetupWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondSetupWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondSetupWindow)

    def retranslateUi(self, SecondSetupWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondSetupWindow.setWindowTitle(_translate("SecondSetupWindow", "Magazyn A"))
        self.przegladajauto.setText(_translate("SecondSetupWindow", "Auta"))
        self.znajdzczesc.setText(_translate("SecondSetupWindow", "Znajdź część"))
        self.dodajczesc.setText(_translate("SecondSetupWindow", "Dodaj część"))
        self.znajdzklienci.setText(_translate("SecondSetupWindow", "Klienci"))
        self.przegladajczesci.setText(_translate("SecondSetupWindow", "Części"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondSetupWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondSetupWindow()
    ui.setupUi(SecondSetupWindow)
    SecondSetupWindow.show()
    sys.exit(app.exec_())