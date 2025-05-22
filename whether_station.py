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
        self.temprature_label = QLabel()
        self.picture_label = QLabel(self)
        self.clear_img = QPixmap("clear.png")
        self.clouds_img = QPixmap("clouds.png")
        self.drizzle_img = QPixmap("drizzle.png")
        self.mist_img = QPixmap("mist.png")
        self.rain_img = QPixmap("rain.png")
        self.snow_img = QPixmap("snow.png")

        self.picture_label.setPixmap(self.clouds_img)
        self.description_label = QLabel()

        self.init_ui()

        self.getWeather_button.clicked.connect(self.get_weather)



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

    def get_weather(self):
        api_key = "1ceb1b8f306bff21e14a821a4f0fccb6"
        city_name = self.city_name_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()


            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Invalid request \nCheck your input")
                case 401:
                    self.display_error("Unauthorized \nInvalid API key")
                case 403:
                    self.display_error("Forbidden \nAccess is denided")
                case 404:
                    self.display_error("Not found \nCity Not found")
                case 500:
                    self.display_error("Internal server Error \nTry again later")
                case 502:
                    self.display_error("Bad gateway \nInvalid response from the server")
                case 503:
                    self.display_error("server unavailable \nServer is down")
                case 504:
                    self.display_error("Gateway time out \nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occured.{http_error}")

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request error.\n {req_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection error.\nCheck Your insternet connection")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirections\n Check the URL")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error.\nThe request time out")


    def display_error(self,message):
        self.temprature_label.setStyleSheet("color: red;")
        self.temprature_label.setText(message)

    def display_weather(self,data):

        temp = (data["main"]["temp"] -273.15).__floor__()
        print(temp)
        self.temprature_label.setText(f"{temp} °C")


        weather_desc = data["weather"][0]["main"]
        self.description_label.setText(weather_desc)

        if weather_desc == "Rain":
            self.picture_label.setPixmap(self.rain_img)
        elif weather_desc == "Clouds":
            self.picture_label.setPixmap(self.clouds_img)
        elif weather_desc == "Drizzle":
            self.picture_label.setPixmap(self.drizzle_img)
        elif weather_desc == "Mist":
            self.picture_label.setPixmap(self.mist_img)
        elif weather_desc == "Clear":
            self.picture_label.setPixmap(self.clear_img)
        elif weather_desc == "Snow":
            self.picture_label.setPixmap(self.snow_img)
        else:
            self.picture_label.setPixmap(self.clear_img)

def main():
    app = QApplication(sys.argv)
    weather_app = wheather_App()
    weather_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()