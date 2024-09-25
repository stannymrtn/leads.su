import pytest
import os


@pytest.fixture()
def base_url():
    return 'https://api.trello.com'
