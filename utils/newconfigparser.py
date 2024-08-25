import configparser
from pathlib import Path

cfgFile = 'qa.ini'
cfgFileDirectory = 'config'

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDirectory).joinpath(cfgFile)

config.read(CONFIG_FILE)

def get_Gmail_Url():
    return (config['gmail']['url'])

def get_Gmail_User():
    return (config['gmail']['user'])

def get_Gmail_Pass():
    return (config['gmail']['pass'])

print(get_Gmail_Url())
