from PyQt5 import QtCore, QtGui, QtWidgets
from szukanie_czesci_part1 import  Ui_SearchPartWindow
from dodawanie_czesci_part1 import Ui_AddPartWindow
from przegladanie_czesci import Ui_ViewPartsWindow
from przegladanie_klienci import Ui_ViewClientsWindow
from przegladanie_auta import Ui_ViewCarsWindow



class Ui_ThirdSetupWindow(object):
    def openWindow(self, number):
        if number == 1:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_AddPartWindow()
            self.ui.setupUi(self.window, 1)
            self.window.show()
        elif number == 2:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_SearchPartWindow()
            self.ui.setupUi(self.window, 1)
            self.window.show()
        elif number == 3:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_ViewPartsWindow()
            self.ui.setupUi(self.window, 1)
            self.window.show()
        elif number == 4:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_ViewClientsWindow()
            self.ui.setupUi(self.window, 1)
            self.window.show()
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_ViewCarsWindow()
            self.ui.setupUi(self.window, 1)
            self.window.show()

    def setupUi(self, ThirdSetupWindow):
        ThirdSetupWindow.setObjectName("ThirdSetupWindow")
        ThirdSetupWindow.resize(750, 500)
        self.centralwidget = QtWidgets.QWidget(ThirdSetupWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.dodajczesc = QtWidgets.QPushButton(self.centralwidget)
        self.dodajczesc.clicked.connect(lambda: self.openWindow(1))
        self.dodajczesc.setGeometry(QtCore.QRect(20, 20, 215, 70))

        self.znajdzczesc = QtWidgets.QPushButton(self.centralwidget)
        self.znajdzczesc.clicked.connect(lambda: self.openWindow(2))
        self.znajdzczesc.setGeometry(QtCore.QRect(20, 110, 215, 70))

        self.dodajauto = QtWidgets.QPushButton(self.centralwidget)
        self.dodajauto.clicked.connect(lambda: self.openWindow(3))
        self.dodajauto.setGeometry(QtCore.QRect(20, 200, 215, 70))

        self.znajdzklienci = QtWidgets.QPushButton(self.centralwidget)
        self.znajdzklienci.clicked.connect(lambda: self.openWindow(4))
        self.znajdzklienci.setGeometry(QtCore.QRect(20, 290, 215, 70))

        self.przegladajczesci = QtWidgets.QPushButton(self.centralwidget)
        self.przegladajczesci.clicked.connect(lambda: self.openWindow(5))
        self.przegladajczesci.setGeometry(QtCore.QRect(20, 380, 215, 70))

        font = QtGui.QFont()
        font.setPointSize(17)
        self.dodajauto.setFont(font)
        self.dodajauto.setObjectName("dodajauto")

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




        ThirdSetupWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ThirdSetupWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 20))
        self.menubar.setObjectName("menubar")
        ThirdSetupWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ThirdSetupWindow)
        self.statusbar.setObjectName("statusbar")
        ThirdSetupWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ThirdSetupWindow)
        QtCore.QMetaObject.connectSlotsByName(ThirdSetupWindow)

    def retranslateUi(self, ThirdSetupWindow):
        _translate = QtCore.QCoreApplication.translate
        ThirdSetupWindow.setWindowTitle(_translate("ThirdSetupWindow", "Magazyn B"))
        self.dodajauto.setText(_translate("ThirdSetupWindow", "Dodaj auto"))
        self.znajdzczesc.setText(_translate("ThirdSetupWindow", "Znajdź część"))
        self.dodajczesc.setText(_translate("ThirdSetupWindow", "Dodaj część"))
        self.znajdzklienci.setText(_translate("ThirdSetupWindow", "Klienci"))
        self.przegladajczesci.setText(_translate("ThirdSetupWindow", "Części"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondSetupWindow = QtWidgets.QMainWindow()
    ui = Ui_ThirdSetupWindow()
    ui.setupUi(SecondSetupWindow)
    SecondSetupWindow.show()
    sys.exit(app.exec_())