from flask import Blueprint, jsonify

bp = Blueprint('v1_examples', __name__)

@bp.route('/example')
def get_examples_v1():
    return jsonify({'message': 'Example from API version 1'})
