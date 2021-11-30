from PyQt5 import QtCore, QtGui, QtWidgets
from MagazynA_mainWindow import Ui_SecondSetupWindow
from MagazynB_mainWindow import Ui_ThirdSetupWindow




class Ui_MainWindow(object):
    def openWindow(self):
        if self.comboBox.currentText() == "Magazyn A":
            self.window = QtWidgets.QMainWindow()
            #self.ui = Ui_SecondWindow()
            self.ui = Ui_SecondSetupWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            #MainWindow.hide()

        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_ThirdSetupWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            #MainWindow.hide()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 310)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 460, 70))
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 110, 460, 70))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Magazyn A")
        self.comboBox.addItem("Magazyn B")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(lambda: self.openWindow())
        self.pushButton.setGeometry(QtCore.QRect(20, 200, 460, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox.setFont(font)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 21))
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
        self.pushButton.setText(_translate("MainWindow", "Połącz"))
        self.label.setText(_translate("MainWindow", "Magazyn części samochodowych"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())