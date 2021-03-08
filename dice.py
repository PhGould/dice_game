import time
import random
from PyQt5 import QtGui, QtWidgets, QtCore


def button_clicked():

    roll_the_dice(low, high)


low = 1
high = 6


def dice_roll(low, high):
    player_roll = random.randint(low, high)
    return player_roll
    # exit()


def computer_roll(low, high):
    computer_result = random.randint(low, high)
    return computer_result


def roll_the_dice():
    alert = QMessageBox()
    alert.setText('You roll the dice...')
    alert.exec_()
    time.sleep(1)
    computer_result = computer_roll(low, high)
    player_roll = dice_roll(low, high)
    if player_roll == computer_result:
        print('tie')
    elif player_roll > computer_result:
        print('you won!')
    else:
        print('you lose')
    print(f'your roll was {player_roll}')
    print(f'the computers roll was {computer_result}')


app = QApplication([])
window = QWidget()

dice_button = QPushButton('Roll the dice')
dice_button.setIcon(QIcon('dice.jpg'))
layout = QVBoxLayout()

layout.addWidget(dice_button)

dice_button.clicked.connect(roll_the_dice)

window.setLayout(layout)

window.show()

app.exec_()

# want_to_roll = input('roll the dice? y/n ')

MainWindow.setObjectName("MainWindow")
MainWindow.resize(800, 600)
centralwidget = QtWidgets.QWidget(MainWindow)
centralwidget.setObjectName("centralwidget")
dice_button = QtWidgets.QPushButton(centralwidget)
dice_button.setGeometry(QtCore.QRect(150, 70, 521, 131))
dice_button.setObjectName("dice_button")
result_label = QtWidgets.QLabel(centralwidget)
result_label.setGeometry(QtCore.QRect(320, 260, 111, 71))
result_label.setObjectName("result_label")
text_box = QtWidgets.QTextBrowser(centralwidget)
text_box.setGeometry(QtCore.QRect(250, 340, 256, 192))
text_box.setObjectName("text_box")
MainWindow.setCentralWidget(centralwidget)
menubar = QtWidgets.QMenuBar(MainWindow)
menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
menubar.setObjectName("menubar")
MainWindow.setMenuBar(menubar)
statusbar = QtWidgets.QStatusBar(MainWindow)
statusbar.setObjectName("statusbar")
MainWindow.setStatusBar(statusbar)

retranslateUi(MainWindow)
QtCore.QMetaObject.connectSlotsByName(MainWindow)
'''
    def retranslateUi( MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        dice_button.setText(_translate("MainWindow", "ROLL DA DICE"))
        result_label.setText(_translate("MainWindow", "Result"))
'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
