import pytest 
from pytest_bdd import scenarios,scenario, given, when, then
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


@given('datatype is set')
def check_typeof_set(setup_set):
    print("This is in Background")
    if not isinstance(setup_set, set):
        pytest.xfail('type of obj is not a set')

@given('set is not empty')
def check_set_not_empty(setup_set):
    print("This is in Background")
    if len(setup_set) == 0:
        pytest.xfail('set is empty')


@given('A set has 3 elem', target_fixture='setup_set01')
def set_elements(setup_set):
    if len(setup_set) == 0:
        pytest.xfail('set of elements is empty')
    elif len(setup_set) > 3:
        while len(setup_set) > 3:
            setup_set.pop()
    return setup_set

@when('Add 2 elem to set')
def add_elements(setup_set):
    setup_set.add('America')
    setup_set.add('Spain')


@then('total is 5 elem')
def total_elem(setup_set):
    print(setup_set)
    assert len(setup_set) == 5




    