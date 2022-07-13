import RNG
import Steam
import subprocess
from platform import system as os_type
from os import system as os_sys


def launch_game(path, game):
    if os_type() == 'Windows':
        subprocess.call(path + "/Steam.exe -applaunch " + game)
    elif os_type() == 'Linux' or os_type() == 'Darwin':
        os_sys('steam steam://rungameid/' + game)
    else:
        print('Error: unable to identify operating system')


def run():
    rng = RNG.RNG()
    steam = Steam.Steam()
    install_path = steam.get_install_path()

    id_list = steam.get_games()
    random_game = rng.rng_list(id_list)

    launch_game(install_path, random_game)


if __name__ == '__main__':
    run()
