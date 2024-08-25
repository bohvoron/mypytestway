import csv
import configparser
from pathlib import Path


dataFile = "data.csv"
cfgFileDirectory = 'data'

config  = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(cfgFileDirectory).joinpath(dataFile)

def get_data():
	with open(DATA_FILE, 'r') as f:
		reader = csv.reader(f)
		next(reader)
		data = [tuple(row)for row in reader]
	return data

print(get_data())