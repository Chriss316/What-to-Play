import RNG
import Steam
import Shortcuts
import window as wtpapp

from threading import Thread
from os import system as os_sys
from platform import system as os_type
from subprocess import call as subp_call
from subprocess import Popen as Subp_open


def launch_steam_game(game):
    if os_type() == 'Windows':
        Subp_open('explorer "steam://rungameid/' + game + '"')
    elif os_type() == 'Linux' or os_type() == 'Darwin':
        os_sys('steam steam://rungameid/' + game)
    else:
        print('Funtion Error: unable to identify operating system')


def launch_other_game(game):
    if type(game) == str:
        subp_call(game)
    else:
        launch_steam_game(game)
    # if os_type() == 'Windows':
    #     subp_call(game)
    # elif os_type() == 'Linux' or os_type() == 'Darwin':
    #     os_sys('steam steam://rungameid/' + game)
    # else:
    #     print('Funtion Error: unable to identify operating system')


def run(parse_type, **kwargs):
    shortcuts_path = kwargs.get('shortcuts', None)
    rng = RNG.RNG()

    # STEAM GAMES
    if parse_type == 'steam':
        steam = Steam.Steam()

        id_list = steam.get_games()
        random_game = rng.rng_list(id_list)

        # Run a new thread to prevent tkinter freezing
        Thread(target=launch_steam_game, args=(random_game,), daemon=True).start()

    # SHORTCUT LIBRARY GAMES
    elif parse_type == 'shortcuts':
        shcts = Shortcuts.Shortcuts(shortcuts_path)
        games_list = shcts.get_games()
        random_game = rng.rng_list(games_list)

        # Run a new thread to prevent tkinter freezing
        Thread(target=launch_other_game, args=(random_game,), daemon=True).start()

    else:
        print('Run Error: Something went wrong')
        return


if __name__ == '__main__':
    wtp = wtpapp.WTPApp(steam=run)
    wtp.build()
