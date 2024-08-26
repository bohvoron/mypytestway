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

