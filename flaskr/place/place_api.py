# from flask import (
#     Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
# )
from flask import Blueprint, request, jsonify
from flaskr import kakao_local
bp = Blueprint('main', __name__, url_prefix='/')
# @bp.route('/api', methods=('GET', 'POST'))
@bp.route('/')
def index():
    return 'Hello ,Python!'
# def search():
#     if request.method == 'POST':
#         x = request.get_json()
#         print(type(x))
#         print(x['x'])
#         return x



@bp.route('/api/v1/place', methods = ['GET', 'POST'])
def search_place():
    if request.method == 'POST':
        kakao = kakao_local.kakao_local_api()
        data = request.get_json()
        x = data['x']
        y = data['y']
        radius = data['radius']
        query = '라면'
        res = kakao.search_keyword(query, x=x, y=y, radius=radius, size=5)['documents']
        res = sorted(res, key=lambda x: int(x['distance']))
        return jsonify(res)

    # user = request.get_json()

    # return jsonify(user['x'])
#
# @app.route('/environments/<language>')
# def environments(language):
#     return jsonify({"language":language})

