# src/tests/conftest.py

import pytest


from src import create_app


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object('src.config.TestingConfig')
    with app.app_context():
        yield app