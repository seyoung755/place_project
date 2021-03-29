# from flask import (
#     Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
# )
from flask import Blueprint, request, jsonify
from flaskr import kakao_local
from pprint import pprint
bp = Blueprint('main', __name__, url_prefix='/')
# @bp.route('/api', methods=('GET', 'POST'))
@bp.route('/')
def index():
    return 'Hello ,Python!'


@bp.route('/api/v1/place', methods = ['GET', 'POST'])
def search_place():
    if request.method == 'GET':
        kakao = kakao_local.kakao_local_api()

        query = ['짜장면', '떡볶이', '양꼬치']
        x = request.args.get('x')
        y = request.args.get('y')
        radius = int(request.args.get('radius'))
        # print(x,y,radius)

        res = []
        for q in query:
            # res.extend(kakao.search_keyword(q, x=x, y=y))
            res.extend(kakao.search_keyword(q, x=x, y=y, radius=radius, size=2)['documents'])
        # pprint(res)
        res = sorted(res, key=lambda x: int(x['distance']))
        return jsonify(res)
