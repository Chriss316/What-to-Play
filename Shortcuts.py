import lnk_helper

from os import listdir, path


class Shortcuts:
    def __init__(self, directory):
        self.dir = directory
        self.games_list = []

        self.generate_games()

    def generate_games(self):
        # Iterate the given directory
        for filename in listdir(self.dir):
            file = path.join(self.dir, filename)

            # CHeck only files
            if path.isfile(file):
                file_extension = path.splitext(file)[1]

                # Check files meet the lookup criteria, .URL and .LNK only
                if file_extension == '.lnk':
                    self.games_list.append(self.read_lnk_path(file))
                elif file_extension == '.url':
                    self.games_list.append(self.read_url_path(file))
                else:  # Pass over any files that don't meet the lookup criteria
                    continue

    def get_games(self):
        return self.games_list

    @staticmethod
    def read_lnk_path(file):
        return lnk_helper.get_target(file)

    @staticmethod
    def read_url_path(file):
        f = open(file, "r")
        lines = f.readlines()

        # Split URL, get last index and remove new line char then return as int
        return int(lines[5].split('/')[-1].replace('\n', ''))

