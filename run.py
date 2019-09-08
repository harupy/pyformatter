import json
from zappa.handler import LambdaHandler


def load_settings(settings_name='zappa_settings.json'):
  with open(settings_name, 'r') as f:
    return json.load(f)


# this is how zappa executes the app function
settings = load_settings()
app = LambdaHandler.import_module_and_get_function(settings['dev']['app_function'])

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='5000', debug=True)
