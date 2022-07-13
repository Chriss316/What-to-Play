import RNG
import Steam
import subprocess
from platform import system as os_sys


def launch_game(path, game):
    if os_sys() == 'Windows':
        subprocess.call(path + "/Steam.exe -applaunch " + game)
    elif os_sys() == 'Linux':
        subprocess.call(path + "/steam -applaunch " + game)
    else:  # Darwin(MacOS)
        print('TODO: Not yet implemented')


def run():
    rng = RNG.RNG()
    steam = Steam.Steam()
    install_path = steam.get_install_path()

    id_list = steam.get_games()
    random_game = rng.rng_list(id_list)

    # print(random_game)
    launch_game(install_path, random_game)


if __name__ == '__main__':
    run()
    # Windows / Linux
    # subprocess.call(r"C:\Program Files (x86)\Steam\Steam.exe -applaunch 413150")
    # Mac
    # steam://run/413150
