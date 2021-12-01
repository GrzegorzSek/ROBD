from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import main


class Ui_ViewClientsWindow(object):
    def setupUi(self, ViewClientsWindow, sql_code, adress):
        p1 = main.DB(adress)
        p1.execute_query(sql_code)
        ViewClientsWindow.setObjectName("ViewClientsWindow")
        ViewClientsWindow.resize(700, 700)
        self.tableWidget = QtWidgets.QTableWidget(ViewClientsWindow)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 660, 660))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Imię", "Nazwisko", "Nr. tel", "Adres", "Kod pocztowy"])
        for line in p1.cur:
            rows = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(rows + 1)
            self.tableWidget.setItem(rows, 0, QTableWidgetItem(line[0]))
            self.tableWidget.setItem(rows, 1, QTableWidgetItem(line[1]))
            self.tableWidget.setItem(rows, 2, QTableWidgetItem(line[2]))
            self.tableWidget.setItem(rows, 3, QTableWidgetItem(line[3]))
            self.tableWidget.setItem(rows, 4, QTableWidgetItem(line[4]))



        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

        self.centralwidget = QtWidgets.QWidget(ViewClientsWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(28)
        ViewClientsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ViewClientsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 21))
        self.menubar.setObjectName("menubar")
        ViewClientsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ViewClientsWindow)
        self.statusbar.setObjectName("statusbar")
        ViewClientsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ViewClientsWindow)
        QtCore.QMetaObject.connectSlotsByName(ViewClientsWindow)

    def retranslateUi(self, ViewClientsWindow):
        _translate = QtCore.QCoreApplication.translate
        ViewClientsWindow.setWindowTitle(_translate("ViewClientsWindow", "Klienci"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewClientsWindow = QtWidgets.QMainWindow()
    ui = Ui_ViewClientsWindow()
    ui.setupUi(ViewClientsWindow)
    ViewClientsWindow.show()
    sys.exit(app.exec_())