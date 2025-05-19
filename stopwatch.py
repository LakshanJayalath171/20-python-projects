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
        self.timeLabel = QLabel("00:00:00",self)
        self.start_button = QPushButton("Start",self)
        self.stop_button = QPushButton("Stop",self)
        self.reset_button = QPushButton("Reset",self)

        self.init_ui()

    def init_ui(self):
        self.setGeometry(400,400,500,150)
        self.setWindowTitle("Stop Watch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.timeLabel)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.reset_button)

        self.setLayout(vbox)

        hbox = QHBoxLayout()

    def start(self):
        pass

    def stop(self):
        pass

    def reset(self):
        pass

    def fomat_time(self,time):
        pass

    def update_displa(self):
        pass

    


def main():
    app =QApplication(sys.argv)
    Stopwatch = stopwatch()
    Stopwatch.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()