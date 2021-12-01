from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import main


class Ui_ViewOrdersContentWindow(object):
    def setupUi(self, ViewOrdersContentWindow, sql_code, adress):
        p1 = main.DB(adress)
        p1.execute_query(sql_code)
        ViewOrdersContentWindow.setObjectName("ViewOrdersContentWindow")
        ViewOrdersContentWindow.resize(700, 700)
        self.tableWidget = QtWidgets.QTableWidget(ViewOrdersContentWindow)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 660, 660))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Nazwa części", "Model"])
        for line in p1.cur:
            print(line)
            rows = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(rows + 1)
            self.tableWidget.setItem(rows, 0, QTableWidgetItem(line[0]))
            self.tableWidget.setItem(rows, 1, QTableWidgetItem(line[1]))



        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)


        self.centralwidget = QtWidgets.QWidget(ViewOrdersContentWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(28)
        ViewOrdersContentWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ViewOrdersContentWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 21))
        self.menubar.setObjectName("menubar")
        ViewOrdersContentWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ViewOrdersContentWindow)
        self.statusbar.setObjectName("statusbar")
        ViewOrdersContentWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ViewOrdersContentWindow)
        QtCore.QMetaObject.connectSlotsByName(ViewOrdersContentWindow)

    def retranslateUi(self, ViewOrdersContentWindow):
        _translate = QtCore.QCoreApplication.translate
        ViewOrdersContentWindow.setWindowTitle(_translate("ViewOrdersContentWindow", "Zawartość zamówienia"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewOrdersContentWindow = QtWidgets.QMainWindow()
    ui = Ui_ViewOrdersContentWindow()
    ui.setupUi(ViewOrdersContentWindow, 1, 1)
    ViewOrdersContentWindow.show()
    sys.exit(app.exec_())