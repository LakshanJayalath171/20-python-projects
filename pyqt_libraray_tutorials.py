import sys
from PyQt5.QtWidgets import  QMainWindow,QApplication,QLabel,QPushButton



class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pyqt 5 tutorial")
        self.setGeometry(0,0,500,500)
        self.initUI()



    def initUI(self):
        button = QPushButton("Click me",self)
        button.setGeometry(120,120,50,50)
        button.clicked.connect(self.onClick)

    def onClick(self):
        print("Button Clicked")

def main():
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()