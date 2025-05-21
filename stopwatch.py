#python stopwatch

import sys
from mimetypes import inited

from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QMainWindow,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import QTime,QTimer,Qt

from pyqt_libraray_tutorials import mainWindow


class stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.timeLabel = QLabel("00:00:00:00",self)
        self.start_button = QPushButton("Start",self)
        self.stop_button = QPushButton("Stop",self)
        self.reset_button = QPushButton("Reset",self)
        self.timer = QTimer()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(400,400,500,150)
        self.setWindowTitle("Stop Watch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.timeLabel)

        self.timeLabel.setAlignment(Qt.AlignCenter)
        self.setLayout(vbox)

        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
        QPushButton,QLabel{
          padding: 20px;
          font-weight: bold;
        }
        QPushButton{
          font-size: 30px;
        }
        QLabel{
          font-size:120px;
          background-color:#686A6C;
          border-radius: 10px;
        }""")

        self.stop_button.setEnabled(False)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

        self.timer.timeout.connect(self.update_display)




    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        pass

    def fomat_time(self,time):
        hour = time.hour()
        minute = time.minute()
        seconds = time.seconds()
        miliseconds = time.msec()
        return f"{hour}:{minute}:{seconds}:{miliseconds}"

    def update_display(self):
        self.time =self.time.addMSecs(10)
        self.timeLabel.setText(self.fomat_time(self.time))


def main():
    app =QApplication(sys.argv)
    Stopwatch = stopwatch()
    Stopwatch.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()