import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit,  QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class wheather_App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.city_name_label = QLabel("Enter The City Name:",self)
        self.city_name_input = QLineEdit(self)
        self.getWeather_button = QPushButton("Get Weather",self)
        self.temprature_label = QLabel("70°C")
        self.picture_label = QLabel(self)
        clear_img = QPixmap("clear.png")
        clouds_img = QPixmap("clouds.png")
        drizzle_img = QPixmap("drizzle.png")
        mist_img = QPixmap("mist.png")
        rain_img = QPixmap("rain.png")

        self.picture_label.setPixmap(clouds_img)
        self.description_label = QLabel("Sunny")
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_name_label)
        vbox.addWidget(self.city_name_input)
        vbox.addWidget(self.getWeather_button)
        vbox.addWidget(self.temprature_label)
        vbox.addWidget(self.picture_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_name_label.setAlignment(Qt.AlignLeft)
        self.temprature_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.picture_label.setAlignment(Qt.AlignCenter)

        self.city_name_label.setObjectName("city_name_label")
        self.city_name_input.setObjectName("city_name_label")
        self.getWeather_button.setObjectName("city_name_label")
        self.temprature_label.setObjectName("city_name_label")
        self.picture_label.setObjectName("city_name_label")
        self.description_label.setObjectName("city_name_label")
        self.setGeometry(400,350,350,330)


        self.setStyleSheet("""
           
           QLabel,QPushButton{
             font-family: calibri;
             
           }
          
           QLabel#city_name_label{
              font-size:22px;
           }
           QLineEdit#city_name_input{
              font-size:30px;
              
           }
           QPushButton#getWeather_button{
              font-size:30px;
              font-weight: bold;
           }
           QLabel#temprature_label{
              font-size: 75px;
              
           }
           QLabel#description_label{
              font-size: 22px;
           }
        """)


def main():
    app = QApplication(sys.argv)
    weather_app = wheather_App()
    weather_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()