# ************************************************************************************************ #
#                                                                                                  #
#                                                _    _ _     _       _                      _     #
#    PongSettings.py                            | |  | | |   (_)     | |                    | |    #
#                                               | |  | | |__  _  __ _| |__  ______ _ _ __ __| |    #
#    By: whighzard <seitealexander@proton.me>   | |/\| | '_ \| |/ _` | '_ \|_  / _` | '__/ _` |    #
#                                               \  /\  / | | | | (_| | | | |/ / (_| | | | (_| |    #
#    Created: 2026/05/17 21:20:49 by whighzard   \/  \/|_| |_|_|\__, |_| |_/___\__,_|_|  \__,_|    #
#    Updated: 2026/05/18 09:51:15 by whighzard                   __/ |                             #
#                                                                                                  #
# ************************************************************************************************ #

from kivy.uix.screenmanager import Screen
from Apps.Pong.PongGame import PongGame

class PongSettings(Screen):
    game = PongGame()
    
    def reset(self):
        self.game.reset_ball()
