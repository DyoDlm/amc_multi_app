# ************************************************************************************************ #
#                                                                                                  #
#                                                _    _ _     _       _                      _     #
#    UiManager.py                               | |  | | |   (_)     | |                    | |    #
#                                               | |  | | |__  _  __ _| |__  ______ _ _ __ __| |    #
#    By: whighzard <seitealexander@proton.me>   | |/\| | '_ \| |/ _` | '_ \|_  / _` | '__/ _` |    #
#                                               \  /\  / | | | | (_| | | | |/ / (_| | | | (_| |    #
#    Created: 2026/05/16 15:55:35 by whighzard   \/  \/|_| |_|_|\__, |_| |_/___\__,_|_|  \__,_|    #
#    Updated: 2026/05/17 21:16:41 by whighzard                   __/ |                             #
#                                                                                                  #
# ************************************************************************************************ #

from imports import *
      
class UiManager(ScreenManager):
    def __init__(self, **kwargs):
        super(UiManager, self).__init__(**kwargs) # Hey Mommy
        self.app_screens = {} # {app_name: main_screen_name}

    def add_app(self, app_instance):
        """
        Every App has to implement a `get_screens()` method
        which returns its screens.
        (The first one is considered the main screen)
        """
        screens = app_instance.get_screens()
        if not screens:
            raise ValueError(
                f"\n\nProbably a name problem... No {app_instance.name} found\n\n"
            )
        main_screen_name = screens[0].name
        self.app_screens[app_instance.name] = main_screen_name
        for screen in screens:
            self.add_widget(screen)

    def switch_to_app(self, app_name):
        """Switches the current screen to the main screen of the given app"""
        if app_name not in self.app_screens:
            raise ScreenManagerException(
                f'\n\nNo {app_name} app found... Try to check dir/files names\n\n'
            )
        self.current = self.app_screens[app_name]
