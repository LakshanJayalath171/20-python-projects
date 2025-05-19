#python PyQt Digital clock

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QVBoxLayout
from PyQt5.QtCore import Qt,QTimer,QTime

class digital_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Digital Cock")
        self.setGeometry(500,500,500,100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.setStyleSheet("background-color:black;")

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size:120px;"
                                      "font-family:arial;"
                                      "color:#26ff00;")

        self.timer.timeout.connect(self.getTime)
        self.timer.start(1000)

        self.getTime()


    def getTime(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)



def main():
    app = QApplication(sys.argv)
    clock = digital_clock()

    clock.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
