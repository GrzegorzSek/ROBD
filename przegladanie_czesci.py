from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import main


class Ui_ViewPartsWindow(object):
    def setupUi(self, ViewPartsWindow, sql_code):
        p1 = main.DB('c##scott/tiger@//192.168.0.8:1521/orcl1')
        p1.execute_query(sql_code)
        ViewPartsWindow.setObjectName("ViewPartsWindow")
        ViewPartsWindow.resize(700, 700)
        self.tableWidget = QtWidgets.QTableWidget(ViewPartsWindow)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 660, 660))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["Nazwa", "Opis", "Model", "Marka", "Magazyn", "Liczba Sztuk"])
        for line in p1.cur:
            rows = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(rows + 1)
            self.tableWidget.setItem(rows, 0, QTableWidgetItem(line[0]))
            self.tableWidget.setItem(rows, 1, QTableWidgetItem(line[1]))
            self.tableWidget.setItem(rows, 2, QTableWidgetItem(line[2]))
            self.tableWidget.setItem(rows, 3, QTableWidgetItem(line[3]))
            self.tableWidget.setItem(rows, 4, QTableWidgetItem(line[4]))
            self.tableWidget.setItem(rows, 5, QTableWidgetItem(line[5]))


        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)

        self.centralwidget = QtWidgets.QWidget(ViewPartsWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(28)
        ViewPartsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ViewPartsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 21))
        self.menubar.setObjectName("menubar")
        ViewPartsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ViewPartsWindow)
        self.statusbar.setObjectName("statusbar")
        ViewPartsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ViewPartsWindow)
        QtCore.QMetaObject.connectSlotsByName(ViewPartsWindow)

    def retranslateUi(self, ViewPartsWindow):
        _translate = QtCore.QCoreApplication.translate
        ViewPartsWindow.setWindowTitle(_translate("ViewPartsWindow", "Części"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewPartsWindow = QtWidgets.QMainWindow()
    ui = Ui_ViewPartsWindow()
    ui.setupUi(ViewPartsWindow)
    ViewPartsWindow.show()
    sys.exit(app.exec_())