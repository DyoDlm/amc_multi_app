# ************************************************************************************************ #
#                                                                                                  #
#                                                _    _ _     _       _                      _     #
#    LabirintoApp.py                            | |  | | |   (_)     | |                    | |    #
#                                               | |  | | |__  _  __ _| |__  ______ _ _ __ __| |    #
#    By: whighzard <seitealexander@proton.me>   | |/\| | '_ \| |/ _` | '_ \|_  / _` | '__/ _` |    #
#                                               \  /\  / | | | | (_| | | | |/ / (_| | | | (_| |    #
#    Created: 2026/05/16 15:18:35 by whighzard   \/  \/|_| |_|_|\__, |_| |_/___\__,_|_|  \__,_|    #
#    Updated: 2026/05/16 16:38:34 by whighzard                   __/ |                             #
#                                                                                                  #
# ************************************************************************************************ #

from imports import *
from Apps.Labirinto.LabirintoGame import LabirintoGame

class LabirintoApp(App):
    def build(self):
        return LabirintoGame()


