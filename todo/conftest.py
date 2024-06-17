import pytest

from .app import create_app


@pytest.fixture()
def app():
    app = create_app()

    # App setup

    yield app

    # App teardown


@pytest.fixture()
def client(app):
    return app.test_client()
