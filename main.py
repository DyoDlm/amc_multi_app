# ************************************************************************************************ #
#                                                                                                  #
#                                                _    _ _     _       _                      _     #
#    main.py                                    | |  | | |   (_)     | |                    | |    #
#                                               | |  | | |__  _  __ _| |__  ______ _ _ __ __| |    #
#    By: whighzard <seitealexander@proton.me>   | |/\| | '_ \| |/ _` | '_ \|_  / _` | '__/ _` |    #
#                                               \  /\  / | | | | (_| | | | |/ / (_| | | | (_| |    #
#    Created: 2026/05/16 11:16:14 by whighzard   \/  \/|_| |_|_|\__, |_| |_/___\__,_|_|  \__,_|    #
#    Updated: 2026/05/18 10:37:48 by whighzard                   __/ |                             #
#                                                                                                  #
# ************************************************************************************************ #

#   Kivy and other standard imports
from imports import App, Builder, Screen, Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

#   My mini apps imports
from Apps.UiManager import UiManager
from Apps.Pong.PongApp import PongApp
#from Apps.Labirinto.LabirintoGame import LabirintoGame

class GameMaster(App):
    def build(self):
        #   initialisation
        self.ui_manager = UiManager()
        self.add_menu_screen()

        # Add your app's class
        self.ui_manager.add_app(PongApp())
        #self.ui_manager.add_app(LabirintoApp())

        return self.ui_manager

    def add_menu_screen(self):
        menu_screen = Screen(name="menu")
        layout = BoxLayout(orientation="vertical")

        #   Add buttons access for apps
        btn_pong = Button(text="Play Pong!", size_hint=(1, 0.2))
        btn_pong.bind(on_press=lambda _: self.ui_manager.switch_to_app("pong"))

        #btn_labirinto = Button(text="Play Labirinto", size_hint=(1, 0.2))
        #btn_labirinto.bind(on_press=lambda _: self.ui_manager.switch_to_app("labirinto"))

        #   Add other widegets
        #   ...

        #   Add to UI the widgets
        layout.add_widget(Label(text="Menu", font_size=30))
        layout.add_widget(btn_pong)
        #layout.add_widget(btn_labirinto)

        menu_screen.add_widget(layout)
        self.ui_manager.add_widget(menu_screen)


if __name__ == "__main__":
    GameMaster().run()
