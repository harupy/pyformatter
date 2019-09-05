from app import create_app
from api import create_api

app = create_app()
api = create_api()
app.register_blueprint(api)


if __name__ == '__main__':
  app.run(debug=True)
