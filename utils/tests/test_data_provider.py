import pytest

from utils.util import get_data

@pytest.mark.parametrize('a,b,c,d', get_data())
def doublecheck_provided_data(a,b,c,d):
    print(d)

