from flask import Blueprint, request, jsonify
import autopep8


def create_api():
  api = Blueprint('api', __name__, url_prefix='/api')

  @api.route('/format')
  def format_code():
    params = request.args.to_dict()
    code = params.pop('code')

    # TODO: add an option which allows users to select autoformat provider (yapf or autopep8)
    new_code = autopep8.fix_code(code, options={**params, 'select': ['E', 'W']})
    return jsonify(code=new_code)

  return api
