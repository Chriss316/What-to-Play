import json
from platform import system as os_sys


class Steam:
    def __init__(self):
        # Variables
        self.app_id_list = []
        self.json_vdf = ''
        self.install_path = ''
        self.vdf_path = ''

        # Functions
        self.find_paths()
        self.convert_vdf()
        self.generate_games(self)

    def find_paths(self):
        if os_sys() == 'Windows':
            self.install_path = 'C:/Program Files (x86)/Steam'
            self.vdf_path = 'C:/Program Files (x86)/Steam/steamapps/libraryfolders.vdf'

        elif os_sys() == 'Linux':
            self.install_path = '$HOME/.steam/bin/'
            self.vdf_path = '$HOME/.steam/steam/steamapps/libraryfolders.vdf'

        else:  # Darwin(MacOS)
            print('TODO: Not yet implemented')
            self.install_path = ''
            self.vdf_path = ''

    def get_install_path(self):
        return self.install_path

    def get_vdf_path(self):
        return self.vdf_path

    def convert_vdf(self):
        f = open(self.vdf_path, 'r')

        # Convert VDF file to a JSON style format
        self.json_vdf = f.read()\
            .replace('\n{', ': {')\
            .replace('"\t\t"', '": "')\
            .replace('\n\t{', ': {')\
            .replace('\n\t\t{', ': {')\
            .replace('\n\t}', '\n\t},')\
            .replace('"\n', '",\n')\
            .replace(',\n\t\t}', '\n\t\t}')\
            .replace('"libraryfolders": ', '')\
            .replace('\t},\n}', '\t}\n}')
        '''
            Explanation of above replaces in order
            1: Bring Open Braces({) up to the same line as the keys and add a colon(:) in front of the braces
            2: Replace Tab Deliminated(\t) Key Value Pair(KVP) with JSON Colon(:) delimination
            3: Bring Nested Open Braces({) up to the same line as the nested keys and add a colon(:) in front of the brace
            4: Do the same as 1 and 3 for double nested keys
            5: Add a comma(,) after all Closing Braces(}) that are only one nest deep
            6: Add a comma(,) after all Value Pairs
            7: Remove the last comma(,) from the last Key Value Pair
            8: Remove the opening Key for the Object
            9: Remove Last comma(,) from the last Object Block
        '''

    @staticmethod
    def generate_games(self):
        json_dict = json.loads(self.json_vdf)

        # Generate a list of all app IDs from the VDF file
        for app_lists in json_dict:
            for apps in json_dict[app_lists]['apps']:
                self.app_id_list.append(apps)

    def get_games(self):
        return self.app_id_list
