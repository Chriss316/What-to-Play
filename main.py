import RNG
import Steam
import window as wtpapp

import threading
from os import system as os_sys
from platform import system as os_type
from subprocess import call as subp_call


def launch_game(path, game):
    if os_type() == 'Windows':
        subp_call(path + "/Steam.exe -applaunch " + game)
    elif os_type() == 'Linux' or os_type() == 'Darwin':
        os_sys('steam steam://rungameid/' + game)
    else:
        print('Funtion Error: unable to identify operating system')


def run():
    rng = RNG.RNG()
    steam = Steam.Steam()
    install_path = steam.get_install_path()

    id_list = steam.get_games()
    random_game = rng.rng_list(id_list)

    # Run a new thread to prevent tkinter freezing
    threading.Thread(target=launch_game, args=(install_path, random_game), daemon=True).start()


if __name__ == '__main__':
    wtp = wtpapp.WTPApp(steam=run)
    wtp.build()
