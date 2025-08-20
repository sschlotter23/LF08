import sys
from functions import convert_num
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton,QGridLayout,QWidget,QLineEdit,QLabel

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Number Converter")

        layout = QGridLayout()

        self.numberEdit = QLineEdit()
        self.numberEdit.setPlaceholderText("Enter a positive integer") 
        layout.addWidget(self.numberEdit,0,1)
        
        self.baseEdit = QLineEdit()
        self.baseEdit.setPlaceholderText("Enter a integer between 0 and 10")
        layout.addWidget(self.baseEdit,0,2)

        calculateButton = QPushButton("calculate")
        layout.addWidget(calculateButton,0,3)
        calculateButton.clicked.connect(self.handle_calculate_button)

        self.resultEdit = QLabel()
        layout.addWidget(self.resultEdit,1,2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def handle_calculate_button(self):
        result = convert_num(int(self.numberEdit.text()),int(self.baseEdit.text()))
        self.resultEdit.setText(str(result))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()