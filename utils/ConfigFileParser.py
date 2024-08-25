import configparser
from pathlib import Path

class ConfigFileParser():
    cfgFile = 'qa.ini'
    cfgFileDirectory = 'config'
    config = configparser.ConfigParser()


    def __init__(self, cfg=cfgFile):
        self.cfgFile= cfg
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.CONFIG_FILE = self.BASE_DIR.joinpath(self.cfgFileDirectory).joinpath(self.cfgFile)
        self.config.read(self.CONFIG_FILE)


    def get_Gmail_Url(self):
        return (self.config['gmail']['url'])

    def get_Gmai_lUser(self):
        return (self.config['gmail']['user'])

    def get_Gmail_Pass(self):
        return (self.config['gmail']['pass'])
    
    def get_Outlook_Url(self):
        return (self.config['outlook']['pass'])

if __name__ == '__main__':
    config = ConfigFileParser('prod.ini')
    print(config.get_Gmail_Url())
    print(config.get_Outlook_Url())

