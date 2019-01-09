import pytest
from fixture.application import Application

@pytest.fixture
# пока не работает @pytest.fixture(scope = "session")

def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
