from flask import Flask, Blueprint, request, jsonify, render_template
from flask_cors import CORS
import autopep8


def to_int_if_possible(x):
  return int(x) if x.isdigit() else x


def create_api():
  api = Blueprint('api', __name__, url_prefix='/api')

  @api.route('/format')
  def format_code():
    # convert integer options (e.g. indent_size and max_line_length)
    # because autopep8 doesn't accept them if they are strings.
    params = {k: to_int_if_possible(v) for k, v in request.args.to_dict().items()}
    code = params.pop('code')

    # TODO: add an option which allows users to choose a code formatter

    # autopep8 ignores some errors (E226, E24, W50, and W690) by default.
    # "select" here reverts these ignored errors.
    # see the official doc for detail: https://github.com/hhatto/autopep8#usage
    new_code = autopep8.fix_code(code, options={**params, 'select': ['E', 'W']})
    return jsonify(code=new_code)

  return api


def create_app():
  app = Flask(__name__, template_folder='./templates')
  CORS(app)

  api = create_api()
  app.register_blueprint(api)

  @app.route('/')
  def index():
    return render_template('index.html')

  return app
