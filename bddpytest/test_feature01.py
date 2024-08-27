import pytest 
from pytest_bdd import scenarios, given, when, then
from pathlib import Path

feature_file_directory = 'bddfeatures'
featureFile = 'newfeature.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(feature_file_directory).joinpath(featureFile)


print(FEATURE_FILE)

scenarios(FEATURE_FILE)

@pytest.fixture()
def setup_set():
    print("\n In fixture... setup() function \n")
    contries = {"Poland","Italy","Ukraine", 'USA', 'Argentina'}
    return contries

@given('A set has 3 elem', target_fixture='setup_seto01')
def set_elements(setup_set):
    if len(setup_set) == 0:
        pytest.xfail('set of elements is empty')
    elif len(setup_set) > 3:
        while len(setup_set) > 3:
            setup_set.pop()
    return setup_set

@when('Add 2 elem to set')
def add_elements(setup_seto01):
    setup_seto01.add('America')
    setup_seto01.add('Spain')


@then('total is 5 elem')
def total_elem(setup_seto01):
    print(setup_seto01)
    assert len(setup_seto01) == 5




    