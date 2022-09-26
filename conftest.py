import pytest
from metadriver import driver_single


@pytest.fixture(scope="module")
def browser(): 
    driver_single.go_to_site()
    yield 
    driver_single.close_driver()