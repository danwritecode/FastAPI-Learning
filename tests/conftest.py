import os

import pytest
from starlette.testclient import TestClient

import main
from config.settings import Settings, get_settings


def get_settings_override():
    return Settings(testing=1)


@pytest.fixture(scope="module")
def test_app():
    # set up
    main.app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as test_client:

        # testing
        yield test_client

    # tear down