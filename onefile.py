import sys
from os import path


def get_rel_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return path.join(sys._MEIPASS, filename)
    else:
        return filename
