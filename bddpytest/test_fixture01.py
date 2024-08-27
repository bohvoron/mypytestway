import pytest 
from pytest_bdd import scenario, scenarios, given, when, then
from pathlib import Path

feature_file_directory = 'bddfeatures'
featureFile = 'number01.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(feature_file_directory).joinpath(featureFile)

scenarios(FEATURE_FILE)

@pytest.fixture()
def setup_set():
    print("\n In fixture... setup() function \n")
    contries = {"Poland","Italy","Ukraine", 'USA', 'Argentina'}
    return contries

@given('have set of 3 Countries', target_fixture='setup_seto01')
def set_elements(setup_set):
    if len(setup_set) == 0:
        pytest.xfail('set of elements is empty')
    elif len(setup_set) > 3:
        while len(setup_set) > 3:
            setup_set.pop()
    return setup_set





    