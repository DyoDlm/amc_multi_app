# ************************************************************************************************ #
#                                                                                                  #
#                                                _    _ _     _       _                      _     #
#    PongUtils.py                               | |  | | |   (_)     | |                    | |    #
#                                               | |  | | |__  _  __ _| |__  ______ _ _ __ __| |    #
#    By: whighzard <seitealexander@proton.me>   | |/\| | '_ \| |/ _` | '_ \|_  / _` | '__/ _` |    #
#                                               \  /\  / | | | | (_| | | | |/ / (_| | | | (_| |    #
#    Created: 2026/05/18 11:31:57 by whighzard   \/  \/|_| |_|_|\__, |_| |_/___\__,_|_|  \__,_|    #
#    Updated: 2026/05/18 13:09:32 by whighzard                   __/ |                             #
#                                                                                                  #
# ************************************************************************************************ #

from imports import *
from kivy.vector import Vector

class PongBall(Widget):
    """ Ball movement : velocity, position """
    velocity_x = NumericProperty(2)
    velocity_y = NumericProperty(2)

    velocity = ReferenceListProperty(velocity_x, velocity_y) # struct de vitesse
 
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos # * --> operateur de deballage
                                        # transforme une liste en arguments individuels

class PongPaddle(Widget):
    """ Paddle control with the accelerometer """
    score = NumericProperty(0)
    acc_x = NumericProperty(0) 
    acc_y = NumericProperty(0)

    def move(self):
        smoothness = 1
        self.center_y += self.acc_y * smoothness

        if self.y < 0:
            self.y = 0
        if self.top > self.parent.height:
            self.top = self.parent.height
    
    def bounce_ball(self, ball, sound):
        """ Args : Ball object , bounce sound """ 
        if self.collide_widget(ball):
            vx = ball.velocity_x
            vy = ball.velocity_y
            
            if sound:
                sound.play()
            else:
                print("\n\nNo sound detected\n\n")
            # bounce offset
            offset = (ball.center_y - self.center_y) / (self.height / 2)

            # new speeds and direction after the bounce
            new_vx = -1 * vx * 1.1
            new_vy = vy + offset
            
            ball.velocity_x = new_vx
            ball.velocity_y = new_vy

class BotPaddle(Widget):
    """ Bot Paddle follows the ball. Impossible to win... """
    score = NumericProperty(0)
    ball = ObjectProperty(None) 

    def move(self):
        smoothness = 0.1
        if self.ball:
            target_y = self.ball.center_y
            self.center_y += (target_y - self.center_y) * smoothness
            if self.y < 0:
                self.y = 0
            if self.top > self.parent.height:
                self.top = self.parent.height

    def bounce_ball(self, ball, sound):
        if self.collide_widget(ball):
            vx = ball.velocity_x
            vy = ball.velocity_y
            if sound:
                sound.play()
            else:
                print("\n\nNo sound detected\n\n")

            offset = (ball.center_y - self.center_y) / (self.height / 2)

            new_vx = -1 * vx * 1.1
            new_vy = vy + offset
            
            ball.velocity_x = new_vx
            ball.velocity_y = new_vy
      

