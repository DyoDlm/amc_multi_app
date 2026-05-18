# ************************************************************************************************ #
#                                                                                                  #
#                                                _    _ _     _       _                      _     #
#    PongGame.py                                | |  | | |   (_)     | |                    | |    #
#                                               | |  | | |__  _  __ _| |__  ______ _ _ __ __| |    #
#    By: whighzard <seitealexander@proton.me>   | |/\| | '_ \| |/ _` | '_ \|_  / _` | '__/ _` |    #
#                                               \  /\  / | | | | (_| | | | |/ / (_| | | | (_| |    #
#    Created: 2026/05/16 15:41:29 by whighzard   \/  \/|_| |_|_|\__, |_| |_/___\__,_|_|  \__,_|    #
#    Updated: 2026/05/18 13:11:34 by whighzard                   __/ |                             #
#                                                                                                  #
# ************************************************************************************************ #

from imports import *
from random import randint
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from plyer import accelerometer

from Apps.Pong.accelerometer.AccelerometerApp import AccelerometerApp
from Apps.Pong.PongUtils import PongBall, PongPaddle, BotPaddle

def load_songs():
    sounds = None
    return sounds

class PongGame(Screen):
    """
        Main class of the game 
        Contains :
            - the ball and reset methods, the serve and the game loop
    """
    ball = ObjectProperty(None) #  reference in .kv
    
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    accelerometer = BooleanProperty(True)

    def __init__(self, **kwargs):
        """ Accelerometer / Sounds initialisation"""
        super().__init__(**kwargs)

        # Accelerometer
        FPS = 60
        self.acc_app = AccelerometerApp()
        self.acc_app.on_start()
        self.acc_app.start_accelerometer()
        Clock.schedule_interval(self.update_accelerometer, 1.0/FPS)

        #   Sounds
        self.sound_score = None
        self.sound_bounce = None
        self.sound_paddle_bounce = None
        try:
            print("\n\nCLAP SOUND DOWNLOADED\n\n")
            self.sound_score = SoundLoader.load('Apps/Pong/sounds/clap.wav')
            self.sound_bounce = SoundLoader.load('Apps/Pong/sounds/bounce.wav')
            self.sound_paddle_bounce = SoundLoader.load('Apps/Pong/sounds/paddle_bounce.wav')
        except:
            print("\n\n NO SOUND FOUND \n\n")
        print(f"sound_score chargé : {self.sound_score}")

    def update_accelerometer(self, dt):
        """ It just get the data (x, y) from acc """
        try:
            acc_x = self.acc_app.get_x()
            acc_y = self.acc_app.get_y()
            
            self.player1.acc_x = acc_x
            self.player1.acc_y = acc_y
        except:
            pass 

    def on_enter(self):
        """ Screen incoming event """
        self.reset_ball()
        self.update_score_labels()
        self.player2.ball = self.ball

    def on_leave(self):
        """ Screen outcome event """
        self.reset_ball()

    def reset_ball(self):
        """ Reset : score, speed and pos"""
        self.game_started = False
        self.round_started = False
        Clock.unschedule(self.update)

        if self.ball:
            self.ball.center = self.center
            self.ball.velocity = Vector(0, 0)

    def reset_round(self):
        """ Reset : speed and pos """
        self.round_started = False
        Clock.unschedule(self.update)
        if self.ball:
            self.ball.center = self.center
            self.ball.velocity = Vector(0, 0)

    def serve_ball(self, vel=None):
        """
            start position of the ball --> the center
            Random angle (contained) for start

            Args : vel --> velocity of the ball
        """
        if not self.round_started:
            self.round_started = True
            self.game_started = True
            self.ball.center = self.center
            if vel:
                self.ball.velocity = Vector(*vel) * 2
            else:
                self.ball.velocity = Vector(5, 0).rotate(randint(45, 135)) * -1
                                       # start angle
            Clock.schedule_interval(self.update, 1.0/60.0)  # clock restart  

    def update_score_labels(self):
        """ Manual score updates"""
        self.ids.score1.text = str(self.player1.score)
        self.ids.score2.text = str(self.player2.score)
    
    def update(self, dt):
        """ main event loop """
        self.ball.move()        
        self.player1.move()
        self.player2.move()

        self.player1.bounce_ball(ball=self.ball, sound=self.sound_paddle_bounce)
        self.player2.bounce_ball(ball=self.ball, sound=self.sound_paddle_bounce)

        # collisions top and bottom 
        if (self.ball.y < 0) or (self.ball.top > self.height):
            if self.sound_bounce:
                self.sound_bounce.play()
            self.ball.velocity_y *= -1  # switch direction

        time_service = 1 # s

        # J2 wins the point 
        if self.ball.x < self.x:
            self.player2.score += 1
            self.update_score_labels()
            if self.sound_score:
                self.sound_score.play()
            self.reset_round()
            Clock.schedule_once(lambda dt: self.serve_ball(vel=(-4, 0)), time_service)

        # J1 wins the point
        if self.ball.right > self.width:
            self.player1.score += 1
            self.update_score_labels()
            if self.sound_score:
                self.sound_score.play()
            self.reset_round()
            Clock.schedule_once(lambda dt: self.serve_ball(vel=(4, 0)), time_service)

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y



