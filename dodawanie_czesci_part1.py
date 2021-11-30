from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddPartWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()





    def setupUi(self, AddPartWindow, sql_code):
        AddPartWindow.setObjectName("AddPartWindow")
        AddPartWindow.resize(500, 310)
        self.centralwidget = QtWidgets.QWidget(AddPartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 460, 70))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(lambda: self.openWindow())
        self.pushButton.setGeometry(QtCore.QRect(20, 200, 460, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        AddPartWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddPartWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 21))
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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddPartWindow = QtWidgets.QMainWindow()
    ui = Ui_AddPartWindow()
    ui.setupUi(AddPartWindow)
    AddPartWindow.show()
    sys.exit(app.exec_())