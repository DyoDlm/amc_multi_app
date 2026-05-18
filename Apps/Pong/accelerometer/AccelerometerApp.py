# ************************************************************************************************ #
#                                                                                                  #
#                                                _    _ _     _       _                      _     #
#    AccelerometerApp.py                        | |  | | |   (_)     | |                    | |    #
#                                               | |  | | |__  _  __ _| |__  ______ _ _ __ __| |    #
#    By: whighzard <seitealexander@proton.me>   | |/\| | '_ \| |/ _` | '_ \|_  / _` | '__/ _` |    #
#                                               \  /\  / | | | | (_| | | | |/ / (_| | | | (_| |    #
#    Created: 2026/05/18 13:33:30 by whighzard   \/  \/|_| |_|_|\__, |_| |_/___\__,_|_|  \__,_|    #
#    Updated: 2026/05/18 13:33:31 by whighzard                   __/ |                             #
#                                                                                                  #
# ************************************************************************************************ #

from imports import *
from kivy.utils import platform
from plyer import accelerometer
import random

x = random.uniform(-10, 10)
y = random.uniform(-10, 10)
z = random.uniform(-10, 10)

print(f'X={x:.2f}   Y={y:.2f}   Z={z:.2f}')

class AccelerometerApp(App):
    x = 0
    y = 0
    def on_start(self):
        self.Te = 1.0
        self.accState = False

        if platform == 'android':
            pass
        else:
            pass
    
    def generate_fake_acceleration(self):
        donnees = []
        for _ in range(3):
            donnees.append(random.uniform(-10, 10))
        return donnees

    def update(self, dt):
        #   acquiert et affiche les donnees
        if platform != 'android':
            acceleration = self.generate_fake_acceleration()
        else:
            acc = accelerometer.acceleration
            if acc is None:
                return 
            acceleration = [v if v is not None else 0.0 for v in acc[:3]]
        self.x =  acceleration[0] 
        self.y = acceleration[1]

    def start_accelerometer(self): 
        Clock.schedule_interval(self.update, self.Te)
        if platform == 'android' or platform == 'linux':
            try:
                accelerometer.enable()
            except Exception as e:
                pass


    def stop_accelerometer(self):
        Clock.unschedule(self.update)
        if platform == 'android' or platform == 'linux':
            try:
                accelerometer.disable()
            except Exception as e:
                pass

    def start_stop(self):
        if (self.accState is False):
            self.accState = True
            self.start_accelerometer()
        else:
            self.accState = False
            self.stop_accelerometer()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


