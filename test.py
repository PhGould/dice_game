
from PyQt5.QtWidgets import *


def top_button_clicked():
    alert = QMessageBox()
    alert.setText('You click the button')
    alert.exec_()


def bottom_button_clicked():
    alert = QMessageBox()
    alert.setText('You click the other button')
    alert.exec_()


app = QApplication([])
window = QWidget()

top_button = QPushButton('text1')
bottom_button = QPushButton('text2')
layout = QVBoxLayout()

layout.addWidget(top_button)
layout.addWidget(bottom_button)

top_button.clicked.connect(top_button_clicked)
bottom_button.clicked.connect(bottom_button_clicked)

window.setLayout(layout)

window.show()

app.exec_()
