import configparser

config = configparser.ConfigParser(allow_no_value=True)
config.read('config.ini')

class Lendo_ini():
    def __init__(self):
        self.email = config.get("FILE_DATA","email")
        self.password = config.get("FILE_DATA","password")
    
