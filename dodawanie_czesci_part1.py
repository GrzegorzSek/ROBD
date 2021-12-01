from PyQt5 import QtCore, QtGui, QtWidgets
import main


class Ui_AddPartWindow(object):
    adress = None;
    def update(self):
        nazwa = self.inputBox1.toPlainText()
        opis = self.inputBox2.toPlainText()
        magazyn_id = self.inputBox3.toPlainText()
        liczba_sztuk = self.inputBox4.toPlainText()
        model_id = self.inputBox5.toPlainText()

        print(nazwa + "-" + opis + "-" + magazyn_id + "-" + liczba_sztuk + "-" +
              model_id)
        p1 = main.DB(self.adress)
        p1.cur.callproc('DODAJ_CZESC', [str(nazwa).lower(), str(opis).lower(), int(magazyn_id), int(liczba_sztuk), int(model_id)])


    def setupUi(self, AddPartWindow, adress):
        self.adress = adress
        AddPartWindow.setObjectName("SearchPartWindow")
        AddPartWindow.resize(250, 350)
        self.centralwidget = QtWidgets.QWidget(AddPartWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 200, 30))

        # I rząd
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 60, 70, 30))

        self.inputBox1 = QtWidgets.QTextEdit(self.centralwidget)
        self.inputBox1.setGeometry((QtCore.QRect(110, 60, 110, 30)))
        txt = self.inputBox1.toPlainText()
        # II rząd
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(20, 100, 70, 30))

        self.inputBox2 = QtWidgets.QTextEdit(self.centralwidget)
        self.inputBox2.setGeometry((QtCore.QRect(110, 100, 110, 30)))
        txt = self.inputBox2.toPlainText()
        # III rząd
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(20, 140, 70, 30))

        self.inputBox3 = QtWidgets.QTextEdit(self.centralwidget)
        self.inputBox3.setGeometry((QtCore.QRect(110, 140, 110, 30)))
        txt = self.inputBox3.toPlainText()
        # IV rząd
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(20, 180, 70, 30))

        self.inputBox4 = QtWidgets.QTextEdit(self.centralwidget)
        self.inputBox4.setGeometry((QtCore.QRect(110, 180, 110, 30)))
        txt = self.inputBox4.toPlainText()
        # V rząd
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(20, 220, 70, 30))

        self.inputBox5 = QtWidgets.QTextEdit(self.centralwidget)
        self.inputBox5.setGeometry((QtCore.QRect(110, 220, 110, 30)))
        txt = self.inputBox5.toPlainText()


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(lambda: self.update())
        self.pushButton.setGeometry(QtCore.QRect(20, 260, 200, 30))

        font = QtGui.QFont()
        font.setPointSize(16)
        #self.inputBox.setFont(font)
        self.label.setFont(font)
        self.label.setObjectName("label")
        #self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        AddPartWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddPartWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 20))
        self.menubar.setObjectName("menubar")
        AddPartWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddPartWindow)
        self.statusbar.setObjectName("statusbar")
        AddPartWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddPartWindow)
        QtCore.QMetaObject.connectSlotsByName(AddPartWindow)

    def retranslateUi(self, AddPartWindow):
        _translate = QtCore.QCoreApplication.translate
        AddPartWindow.setWindowTitle(_translate("AddPartWindow", "Dodawanie części"))
        self.pushButton.setText(_translate("AddPartWindow", "Dodaj"))
        self.label.setText(_translate("AddPartWindow", "Dodaj część"))
        self.label1.setText(_translate("AddPartWindow", "Nazwa"))
        self.label2.setText(_translate("AddPartWindow", "Opis"))
        self.label3.setText(_translate("AddPartWindow", "Magazyn_id"))
        self.label4.setText(_translate("AddPartWindow", "Liczba sztuk"))
        self.label5.setText(_translate("AddPartWindow", "Model_id"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchPartWindow = QtWidgets.QMainWindow()
    ui = Ui_AddPartWindow()
    ui.setupUi(SearchPartWindow, 1)
    SearchPartWindow.show()
    sys.exit(app.exec_())