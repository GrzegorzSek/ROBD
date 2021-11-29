import PyQt5.QtWidgets as Qtw
import PyQt5.QtGui as Qtg
from PyQt5 import QtCore, QtGui, QtWidgets
from window2 import Ui_SecondWindow

class MainWindow(Qtw.QWidget):

    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle("Magazyn części zamiennych do samochodów")

        # Set vertical layout
        self.setLayout(Qtw.QVBoxLayout())

        # Create a label
        my_label = Qtw.QLabel("Magazyn części zamiennych do samochodów")
        # change font size of label
        my_label.setFont(Qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)

        # Create combo box
        my_combo = Qtw.QComboBox(self)
        # Add items To The Combo Box
        my_combo.addItem("Magazyn A")
        my_combo.addItem("Magazyn B")
        my_combo.addItem("Admin")
        self.layout().addWidget(my_combo)

        # Create a button
        my_button = Qtw.QPushButton("Połącz")
        my_button.clicked.connect(lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            # Add name to label
            my_label.setText(f"Hello {my_combo.currentText()}")



app = Qtw.QApplication([])
mw = MainWindow()

# Run the app
app.exec_()
