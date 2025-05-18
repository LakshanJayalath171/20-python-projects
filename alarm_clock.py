# Python alarm clock
import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Set Alarm for {alarm_time}")
    soud_file = "music01.mp3"
    is_running = True


    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)

        if alarm_time == current_time:
            print("Wake Up!! 😫")
            pygame.mixer.init()
            pygame.mixer.music.load(soud_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running =False

def main():


    alarm_time = input("Enter A Alarm Time(HH:MM:SS): ")
    set_alarm(alarm_time)
if __name__ == '__main__':
    main()

