import LogList
import ParserSettings


class ParserUI:
    def __init__(self):
        self.logs = LogList.LogList()
        self.parser_setting = ParserSettings.ParserSettings()

    def run(self):
        # Attempt to load default parser settings
        try:
            self.parser_setting.read("cfg/default_setting.cfg")
        except FileNotFoundError:
            print("Default settings cannot be found!")
            print("Generating new default settings...\n")
            self.generate_new_default_setting()

        # Prompt user for input
        while True:
            print("(L)oad new parser settings")
            print("(S)ave current parser settings")
            print("(E)dit parser settings")
            print("(N)ew parser operation")
            print("(Q)uit")
            user_input = str(input(">"))

    def quit(self):
        pass

    def load_file(self, filename):
        pass

    def load_files(self, folder):
        pass

    def generate_new_default_setting(self):
        self.parser_setting.write("cfg/default_setting.cfg")
