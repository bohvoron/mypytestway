import pytest 
from pytest_bdd import scenarios,scenario, given, when, then, parsers
from pathlib import Path

feature_file_directory = 'bddfeatures'
featureFile = 'param.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(feature_file_directory).joinpath(featureFile)


print(FEATURE_FILE)

scenarios(FEATURE_FILE)

@given('4 variaties cars', target_fixture='cars')
def set_up():
    cars = {'BMW','Audi','Nissan','Ford'}
    return cars

@when('add same variaty')
def add_car(cars):
    cars.add('Nissan')

@then('same count of cars')
def count_cars(cars):
    assert len(cars) == 4

@then('if we add a some different variaty')
def add_diff_car(cars):
    cars.add('Porshe')

@then(parsers.parse('Count increases to {count:d}'))
def increase_function(cars, count):
    assert len(cars) == count



@given(parsers.parse('Given a {count:d} cars'),target_fixture='start_cars')
def cars_five(count):
    return dict(start=count, gave=0)


@when(parsers.parse('I gave {gave:d} cars to cousin'))
def gave_3_sister(start_cars,gave):
    print(start_cars)
    start_cars['gave'] += gave
   
@when(parsers.parse('I gave {gave:d} cars to cousen'))
def gave_2_brother(start_cars,gave):
    print(start_cars)
    start_cars['gave'] += gave

@then(parsers.parse('I have {total:d} cars for gifts'))
def left_for_gifts(start_cars,total):
     print(start_cars)
     assert start_cars['start'] - start_cars['gave'] == total