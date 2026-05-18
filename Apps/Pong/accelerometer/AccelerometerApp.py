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
        self.Te = 1.0 # periode d'echantillonage
        self.accState = False

        if platform == 'android':
            pass
        ##self.root.ids.debug_label.text = 'Plateforme : Android'
        else:
            pass
            #self.root.ids.debug_label.text = f'Plateforme : {platform} (simulation)'
    
    def generate_fake_acceleration(self):
        donnees = []
        for _ in range(3):
            donnees.append(random.uniform(-10, 10))
        return donnees

    def update(self, dt):
        #   acquiert et affiche les donnees
        if platform != 'android':
            print("Generating fake acc")
            acceleration = self.generate_fake_acceleration()
        else:
            acc = accelerometer.acceleration
            print("Are we in android ?? ")
            if acc is None:
                return 
            acceleration = [v if v is not None else 0.0 for v in acc[:3]]
        #self.root.ids.acc_label.text = (
        #        'X= %.2f\nY= %.2f\nZ= %.2f' % tuple(acceleration)
 #AttributeError: 'AccelerometerApp' object has no attribute 'Te'
  #              )
        self.x =  acceleration[0] #acceleration
        self.y = acceleration[1]
        #print(self.x, self.y)

    def start_accelerometer(self):
         
        Clock.schedule_interval(self.update, self.Te)
        if platform == 'android' or platform == 'linux':
            try:
                accelerometer.enable()
                #self.root.ids.debug_label.text = 'Accelerometre actif'
            except Exception as e:
                pass
            #   self.root.ids.debug_label.text = f'Erreur: {e}'


    def stop_accelerometer(self):
        Clock.unschedule(self.update)
        if platform == 'android' or platform == 'linux':
            try:
                accelerometer.disable()
                #self.root.ids.debug_label.text = 'Accelerometre inactif'
            except Exception as e:
                pass #self.root.ids.debug_label.text = f'Erreur: {e}'

    def start_stop(self):
        if (self.accState is False):
            self.accState = True
            self.start_accelerometer()
        else:
            self.accState = False
            self.stop_accelerometer()
        print("Button Start/Stop clicked")

    def get_x(self):
        #print(f"X is : {self.X}")
        return self.x

    def get_y(self):
        #print(f"Y is : {self.Y}")
        return self.y


