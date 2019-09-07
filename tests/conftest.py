import pytest
from app.factory import create_app, create_api


@pytest.fixture
def app():
  app = create_app()
  api = create_api()
  app.register_blueprint(api)
  app.testing = True
  return app


@pytest.fixture
def client(app):
  return app.test_client()
