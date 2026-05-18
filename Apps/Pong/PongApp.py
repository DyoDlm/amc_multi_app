# ************************************************************************************************ #
#                                                                                                  #
#                                                _    _ _     _       _                      _     #
#    PongApp.py                                 | |  | | |   (_)     | |                    | |    #
#                                               | |  | | |__  _  __ _| |__  ______ _ _ __ __| |    #
#    By: whighzard <seitealexander@proton.me>   | |/\| | '_ \| |/ _` | '_ \|_  / _` | '__/ _` |    #
#                                               \  /\  / | | | | (_| | | | |/ / (_| | | | (_| |    #
#    Created: 2026/05/16 15:18:35 by whighzard   \/  \/|_| |_|_|\__, |_| |_/___\__,_|_|  \__,_|    #
#    Updated: 2026/05/18 08:35:07 by whighzard                   __/ |                             #
#                                                                                                  #
# ************************************************************************************************ #

from imports import *

from Apps.Pong.PongUI import PongUI
from Apps.Pong.PongGame import PongGame
from Apps.Pong.PongSettings import PongSettings

class PongApp:
    def __init__(self):
        self.name = "pong"  # name used in the UiManager

    def get_screens(self):
        """
            Returns all screens of the app.
            (first screen is considered the main screen)
        """
        Builder.load_file("Apps/Pong/pong.kv")

        pong_ui_screen          = PongUI(name="pong_ui")
        pong_game_screen        = PongGame(name="pong_game")
        pong_settings_screen    = PongSettings(name="pong_settings")

        return [pong_ui_screen, pong_game_screen, pong_settings_screen]

