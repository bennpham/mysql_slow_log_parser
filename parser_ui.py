import Parser
import ParserSettings


class ParserUI:
    def __init__(self):
        self.parser = Parser.Parser()
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
        self.prompt_screen1()

    def prompt_screen1(self):
        while True:
            print("(L)oad new parser settings")
            print("(S)ave current parser settings")
            print("(E)dit parser settings")
            print("(N)ew parser operation")
            print("(Q)uit")
            user_input = str(input(">"))

            # Load New Parser Settings
            if user_input.lower().strip() == 'l':
                self.load_new_parser_settings()
            # Save Current Parser Settings
            elif user_input.lower().strip() == 's':
                self.save_current_parser_settings()
            # Edit Parser Settings
            elif user_input.lower().strip() == 'e':
                pass
            # New Parser Operation
            elif user_input.lower().strip() == 'n':
                pass
            # Quit
            elif user_input.lower().strip() == 'q':
                break

    def load_new_parser_settings(self):
        print("Type in the path and filename of the parser settings.")
        print("Note: .cfg path is appended to the end of the file automatically. Do not specify the file extension.")
        user_input = str(input(">"))
        try:
            self.parser_setting.read(user_input + ".cfg")
        except FileNotFoundError:
            print("Error: File does not exist!")
        except OSError:
            print("Error: Invalid filename!")

    def save_current_parser_settings(self):
        print("Type in the path and filename to save the current parser settings.")
        print("Press Enter without typing any filename to save to default settings.")
        print("Note: .cfg path is appended to the end of the file automatically. Do not specify the file extension.")
        user_input = str(input(">"))
        if user_input == "":
            self.generate_new_default_setting()
        else:
            try:
                self.parser_setting.write(user_input + ".cfg")
            except FileNotFoundError:
                print("Error: File does not exist!")
            except OSError:
                print("Error: Invalid filename!")

    def load_file(self, filename):
        pass

    def load_files(self, folder):
        pass

    def generate_new_default_setting(self):
        self.parser_setting.write("cfg/default_setting.cfg")
