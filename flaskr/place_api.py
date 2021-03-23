from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)

bp = Blueprint('place', __name__)
@bp.route('/api', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        x = request.get_json()
        print(type(x))
        print(x['x'])
        return x



# @app.route('/api/v1/place', methods = ['POST'])
# def search_place():
#     user = request.get_json()
#     return jsonify(user)
#
# @app.route('/environments/<language>')
# def environments(language):
#     return jsonify({"language":language})

