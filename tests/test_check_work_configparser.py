from utils.newconfigparser import *
from utils.ConfigFileParser import ConfigFileParser

config = ConfigFileParser('prod.ini')



def test_check_get_Gmail_Url():
    print(get_Gmail_Url())

def test_get_Outlook_Url():
    print(get_Outlook_Url())