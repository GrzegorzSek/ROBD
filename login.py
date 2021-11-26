import PyQt5.QtWidgets as Qtw
import PyQt5.QtGui as Qtg


class MainWindow(Qtw.QWidget):

    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle("Magazyn części zamiennych do samochodów")

        # Set vertical layout
        self.setLayout(Qtw.QVBoxLayout())

        # Create a label
        my_label = Qtw.QLabel("Magazyn części zamiennych do samochodów")
        self.layout().addWidget(my_label)

        # change font size of label
        my_label.setFont(Qtg.QFont('Helvetica', 18))

        # Create entry box
        my_entry = Qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("Placeholder")
        self.layout().addWidget(my_entry)

        def press_it():
            # Add name to label
            my_label.setText(f'Hello {my_entry.text()}')
            # Clear the entry box
            my_entry.setText("")

        my_button = Qtw.QPushButton("Połącz")
        my_button.clicked.connect(press_it)
        self.layout().addWidget(my_button)

        self.show()




app = Qtw.QApplication([])
mw = MainWindow()

# Run the app
app.exec_()
