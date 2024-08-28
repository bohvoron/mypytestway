import pytest 
from pytest_bdd import scenario, given, when, then, parsers
from pathlib import Path

feature_file_directory = 'bddfeatures'
featureFile = 'scenariooutline.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(feature_file_directory).joinpath(featureFile)


scenario(FEATURE_FILE, 'Scenario outline')
def test_outline():
    pass


@given(parsers.parse('There are {start:d} cars'), target_fixture='cars')
def existing_cars(start):
    return dict(start=start)

@when(parsers.parse('I deposit {deposit:d} cars'))
def deposit_cars(cars, deposit):
    cars['deposit'] = deposit
    print(cars)

@when(parsers.parse('I withdraw {withdraw:d} cars'))
def withdraw_cars(cars,withdraw):
    cars[withdraw] = withdraw
    print(cars)

@then(parsers.parse('I have {finall:d} cars'))
def finall_count_cars(cars,finall):
    cars[finall] = finall
    print(cars)
