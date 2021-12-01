from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import main


class Ui_ViewCarsWindow(object):
    def setupUi(self, ViewCarsWindow, sql_code, adress):
        p1 = main.DB(adress)
        p1.execute_query(sql_code)
        ViewCarsWindow.setObjectName("ViewCarsWindow")
        ViewCarsWindow.resize(700, 700)
        self.tableWidget = QtWidgets.QTableWidget(ViewCarsWindow)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 660, 660))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Marka", "Model"])
        for line in p1.cur:
            rows = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(rows + 1)
            self.tableWidget.setItem(rows, 0, QTableWidgetItem(line[0]))
            self.tableWidget.setItem(rows, 1, QTableWidgetItem(line[1]))



        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)


        self.centralwidget = QtWidgets.QWidget(ViewCarsWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(28)
        ViewCarsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ViewCarsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 21))
        self.menubar.setObjectName("menubar")
        ViewCarsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ViewCarsWindow)
        self.statusbar.setObjectName("statusbar")
        ViewCarsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ViewCarsWindow)
        QtCore.QMetaObject.connectSlotsByName(ViewCarsWindow)

    def retranslateUi(self, ViewCarsWindow):
        _translate = QtCore.QCoreApplication.translate
        ViewCarsWindow.setWindowTitle(_translate("ViewCarsWindow", "Auta"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewCarsWindow = QtWidgets.QMainWindow()
    ui = Ui_ViewCarsWindow()
    ui.setupUi(ViewCarsWindow)
    ViewCarsWindow.show()
    sys.exit(app.exec_())