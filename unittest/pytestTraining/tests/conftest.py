import pytest
@pytest.fixture(autouse=True, scope='function')
def setup_teardown():
    print('Starting..')
    yield
    print('Ending..')

