import sys
from PyQt5.QtWidgets import  QMainWindow,QApplication,QRadioButton,QButtonGroup
from PyQt5.QtCore import Qt



class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pyqt 5 tutorial")
        self.setGeometry(0,0,500,500)
        self.radioButton01 = QRadioButton("Visa",self)
        self.radioButton02 = QRadioButton("Master card", self)
        self.radioButton03 = QRadioButton("paypal", self)
        self.radioButton04 = QRadioButton("American Express", self)
        self.radioButton05 = QRadioButton("Apple pay",self)

        self.buttn_group01 = QButtonGroup(self)
        self.buttn_group02 = QButtonGroup(self)
        self.initUI()



    def initUI(self):
        self.radioButton01.setGeometry(0,0,300,50)
        self.radioButton02.setGeometry(0, 50, 300, 50)
        self.radioButton03.setGeometry(0, 100, 300, 50)
        self.radioButton04.setGeometry(0, 150, 300, 50)
        self.radioButton05.setGeometry(0, 200, 300, 50)

        self.setStyleSheet("QRadioButton{"
                           "font-size:25px;"
                           "font-family:poppins;"
                           "padding:10px;}")

        self.buttn_group01.addButton(self.radioButton01)
        self.buttn_group01.addButton(self.radioButton02)
        self.buttn_group01.addButton(self.radioButton03)
        self.buttn_group02.addButton(self.radioButton04)
        self.buttn_group02.addButton(self.radioButton05)

        self.radioButton01.toggled.connect(self.onClick)
        self.radioButton02.toggled.connect(self.onClick)
        self.radioButton03.toggled.connect(self.onClick)
        self.radioButton04.toggled.connect(self.onClick)
        self.radioButton05.toggled.connect(self.onClick)



    def onClick(self):
        radio_button = self.sender()

        if radio_button.isChecked():
            paring


def main():
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()