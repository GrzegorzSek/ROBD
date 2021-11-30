from PyQt5 import QtCore, QtGui, QtWidgets
from przegladanie_czesci import Ui_ViewPartsWindow


class Ui_SearchPartWindow(object):
    def openWindow(self):
        txt = self.inputBox.toPlainText()
        print(txt)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ViewPartsWindow()
        self.ui.setupUi(self.window, 1)
        self.window.show()


    def setupUi(self, SearchPartWindow, sql_code):
        SearchPartWindow.setObjectName("SearchPartWindow")
        SearchPartWindow.resize(500, 410)
        self.centralwidget = QtWidgets.QWidget(SearchPartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 460, 70))

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 110, 460, 70))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Nazwa")
        self.comboBox.addItem("Model")

        self.inputBox = QtWidgets.QTextEdit(self.centralwidget)
        self.inputBox.setGeometry((QtCore.QRect(20, 200, 460, 70)))
        txt = self.inputBox.toPlainText()


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(lambda: self.openWindow())
        self.pushButton.setGeometry(QtCore.QRect(20, 290, 460, 70))

        font = QtGui.QFont()
        font.setPointSize(16)
        self.inputBox.setFont(font)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        SearchPartWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SearchPartWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 21))
        self.menubar.setObjectName("menubar")
        SearchPartWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SearchPartWindow)
        self.statusbar.setObjectName("statusbar")
        SearchPartWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SearchPartWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchPartWindow)

    def retranslateUi(self, SearchPartWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchPartWindow.setWindowTitle(_translate("SearchPartWindow", "Szukanie części"))
        self.pushButton.setText(_translate("SearchPartWindow", "Szukaj"))
        self.label.setText(_translate("SearchPartWindow", "Wyszukaj część"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchPartWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchPartWindow()
    ui.setupUi(SearchPartWindow, 1)
    SearchPartWindow.show()
    sys.exit(app.exec_())