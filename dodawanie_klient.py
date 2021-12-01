from PyQt5 import QtCore, QtGui, QtWidgets
import main


class Ui_AddClientWindow(object):
    adress = None
    def update(self):
        imie = self.inputBox1.toPlainText()
        nazwisko = self.inputBox2.toPlainText()
        Nr_tel = self.inputBox3.toPlainText()
        adres = self.inputBox4.toPlainText()
        kod_pocztowy = self.inputBox5.toPlainText()

        try:
            print(imie + "-" + nazwisko + "-" + Nr_tel + "-" + adres + "-" +
                  kod_pocztowy)
            p1 = main.DB(self.adress)
            p1.cur.callproc('DODAJ_KLIENTA', [str(imie).lower(), str(nazwisko).lower(), str(Nr_tel), str(adres).lower(), str(kod_pocztowy).lower()])
        except:
            print("Błąd przy dodawaniu klienta")


    def setupUi(self, AddClientWindow, adress):
        self.adress = adress
        AddClientWindow.setObjectName("AddClientWindow")
        AddClientWindow.resize(350, 350)
        self.centralwidget = QtWidgets.QWidget(AddClientWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 200, 30))

        # I rząd
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 60, 70, 30))

        self.inputBox1 = QtWidgets.QTextEdit(self.centralwidget)
        self.inputBox1.setGeometry((QtCore.QRect(130, 60, 110, 30)))
        txt = self.inputBox1.toPlainText()
        # II rząd
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(20, 100, 70, 30))

        self.inputBox2 = QtWidgets.QTextEdit(self.centralwidget)
        self.inputBox2.setGeometry((QtCore.QRect(130, 100, 110, 30)))
        txt = self.inputBox2.toPlainText()
        # III rząd
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(20, 140, 70, 30))

        self.inputBox3 = QtWidgets.QTextEdit(self.centralwidget)
        self.inputBox3.setGeometry((QtCore.QRect(130, 140, 110, 30)))
        txt = self.inputBox3.toPlainText()
        # IV rząd
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(20, 180, 70, 30))

        self.inputBox4 = QtWidgets.QTextEdit(self.centralwidget)
        self.inputBox4.setGeometry((QtCore.QRect(130, 180, 110, 30)))
        txt = self.inputBox4.toPlainText()
        # V rząd
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(20, 220, 90, 30))

        self.inputBox5 = QtWidgets.QTextEdit(self.centralwidget)
        self.inputBox5.setGeometry((QtCore.QRect(130, 220, 110, 30)))
        txt = self.inputBox5.toPlainText()


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(lambda: self.update())
        self.pushButton.setGeometry(QtCore.QRect(20, 260, 220, 30))

        font = QtGui.QFont()
        font.setPointSize(16)
        #self.inputBox.setFont(font)
        self.label.setFont(font)
        self.label.setObjectName("label")
        #self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        AddClientWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddClientWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 20))
        self.menubar.setObjectName("menubar")
        AddClientWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddClientWindow)
        self.statusbar.setObjectName("statusbar")
        AddClientWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddClientWindow)
        QtCore.QMetaObject.connectSlotsByName(AddClientWindow)

    def retranslateUi(self, AddClientWindow):
        _translate = QtCore.QCoreApplication.translate
        AddClientWindow.setWindowTitle(_translate("AddClientWindow", "Dodawanie klienta"))
        self.pushButton.setText(_translate("AddClientWindow", "Dodaj"))
        self.label.setText(_translate("AddClientWindow", "Dodaj klienta"))
        self.label1.setText(_translate("AddClientWindow", "Imie"))
        self.label2.setText(_translate("AddClientWindow", "Nazwisko"))
        self.label3.setText(_translate("AddClientWindow", "Nr. telefonu"))
        self.label4.setText(_translate("AddClientWindow", "Adres"))
        self.label5.setText(_translate("AddClientWindow", "Kod pocztowy"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchClientWindow = QtWidgets.QMainWindow()
    ui = Ui_AddClientWindow()
    ui.setupUi(SearchClientWindow, 1)
    SearchClientWindow.show()
    sys.exit(app.exec_())