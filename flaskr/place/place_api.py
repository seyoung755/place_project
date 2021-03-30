# from flask import (
#     Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
# )
from flask import Blueprint, request, jsonify
from flaskr import kakao_local
from pprint import pprint
from flaskr import location_code_fetcher
from flaskr import weather_api
bp = Blueprint('main', __name__, url_prefix='/')
# @bp.route('/api', methods=('GET', 'POST'))
@bp.route('/')
def index():
    return 'Hello ,Python!'


@bp.route('/api/v1/place', methods = ['GET', 'POST'])
def search_place():
    if request.method == 'GET':
        kakao = kakao_local.kakao_local_api()

        # query = ['짜장면', '떡볶이', '양꼬치']
        x = request.args.get('x')
        y = request.args.get('y')
        radius = int(request.args.get('radius'))

        grid_x, grid_y = location_code_fetcher.mapToGrid(float(y), float(x))
        weather = weather_api.today_weather(str(grid_x), str(grid_y))


        query = {"맑음" : ["치킨", "피자", "탕수육", "고기"],
                 "더움" : ["냉면", "빙수", "아이스크림", "밀면"],
                 "추움" : ["우동", "라멘", "라면", "샤브샤브", "국물"],
                 "비" : ["막걸리", "파전"]}



        res = []

        for q in query[weather]:
            res.extend(kakao.search_keyword(q, x=x, y=y, radius=radius, size=2)['documents'])
        # pprint(res)
        res = sorted(res, key=lambda x: int(x['distance']))
        res.insert(0, weather)
        return jsonify(res)
