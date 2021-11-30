from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import main


class Ui_ThirdWindow(object):
    def setupUi(self, ThirdWindow):
        p1 = main.DB('c##scott/tiger@//192.168.0.8:1521/orcl1')
        p1.execute_query("""SELECT * FROM TEST_VIEW""")
        ThirdWindow.setObjectName("ThirdWindow")
        ThirdWindow.resize(700, 700)
        self.tableWidget = QtWidgets.QTableWidget(ThirdWindow)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 660, 660))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Wartość"])
        for line in p1.cur:
            rows = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(rows + 1)
            self.tableWidget.setItem(rows, 0, QTableWidgetItem(line[1]))
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.centralwidget = QtWidgets.QWidget(ThirdWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(28)
        ThirdWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ThirdWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 21))
        self.menubar.setObjectName("menubar")
        ThirdWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ThirdWindow)
        self.statusbar.setObjectName("statusbar")
        ThirdWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ThirdWindow)
        QtCore.QMetaObject.connectSlotsByName(ThirdWindow)

    def retranslateUi(self, ThirdWindow):
        _translate = QtCore.QCoreApplication.translate
        ThirdWindow.setWindowTitle(_translate("ThirdWindow", "Magazyn B"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ThirdWindow = QtWidgets.QMainWindow()
    ui = Ui_ThirdWindow()
    ui.setupUi(ThirdWindow)
    ThirdWindow.show()
    sys.exit(app.exec_())