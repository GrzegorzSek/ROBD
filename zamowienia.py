from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import main


class Ui_ViewOrdersWindow(object):
    def setupUi(self, ViewOrdersWindow, sql_code, adress):
        p1 = main.DB(adress)
        p1.execute_query(sql_code)
        ViewOrdersWindow.setObjectName("ViewOrdersWindow")
        ViewOrdersWindow.resize(700, 700)
        self.tableWidget = QtWidgets.QTableWidget(ViewOrdersWindow)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 660, 660))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["ID zamówienia", "Kwota", "Data złożenia", "Dodatkowy opis"])
        for line in p1.cur:
            print(line)
            rows = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(rows + 1)
            self.tableWidget.setItem(rows, 0, QTableWidgetItem(str(line[0])))
            self.tableWidget.setItem(rows, 1, QTableWidgetItem(str(line[1])))
            self.tableWidget.setItem(rows, 2, QTableWidgetItem(str(line[2])))
            self.tableWidget.setItem(rows, 3, QTableWidgetItem(line[3]))


        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        self.centralwidget = QtWidgets.QWidget(ViewOrdersWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(28)
        ViewOrdersWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ViewOrdersWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 21))
        self.menubar.setObjectName("menubar")
        ViewOrdersWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ViewOrdersWindow)
        self.statusbar.setObjectName("statusbar")
        ViewOrdersWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ViewOrdersWindow)
        QtCore.QMetaObject.connectSlotsByName(ViewOrdersWindow)

    def retranslateUi(self, ViewOrdersWindow):
        _translate = QtCore.QCoreApplication.translate
        ViewOrdersWindow.setWindowTitle(_translate("ViewOrdersWindow", "Zamówienia"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewOrdersWindow = QtWidgets.QMainWindow()
    ui = Ui_ViewOrdersWindow()
    ui.setupUi(ViewOrdersWindow, 1, 1)
    ViewOrdersWindow.show()
    sys.exit(app.exec_())