import pytest 
from pytest_bdd import scenario, scenarios, given, when, then
from pathlib import Path

feature_file_directory = 'bddfeatures'
featureFile = 'number01.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(feature_file_directory).joinpath(featureFile)


def pytest_configure():
    pytest.AMT = 0

@scenario(FEATURE_FILE, 'Withdrawal of money')
def test_withdrawal():
    print('End of test Withdrawal')
    pass

@given('The balance is 1000')
def current_balance():
    pytest.AMT = 1000


@when('the acc holder withdraws 300')
def withdraw_balance():
    pytest.AMT = pytest.AMT - 300

@then('balans should to be 700')
def final_balance():
    assert pytest.AMT == 700






@scenario(FEATURE_FILE, 'Remove fruits with set')
def test_remove_fruit():
    print('End of test Remove')
    pass


@given('have set of 4 fruits', target_fixture="my_set")
def start_fruits_number():
    my_set = {'banana','apple','cherry','pineapple'}
    return my_set

@when('We remove 1 fruit from a set')
def remove_fruit(my_set):
    my_set.pop()
    print(my_set)

@then('finall set has 3 fruits')
def final_fruit_number(my_set):
    assert (len(my_set)) == 3