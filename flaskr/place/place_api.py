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
        # 위도, 경도를 격자 좌표로 변환
        try:
            grid_x, grid_y = location_code_fetcher.mapToGrid(float(y), float(x))
        except Exception as e:
            return jsonify(e)

        # 날씨 api로부터 날씨 수신
        weather = weather_api.today_weather(str(grid_x), str(grid_y))

        # 날씨 별 keyword 정리 => weather_api 로 이동

        res = []

        for q in weather_api.query.setdefault(weather, "맑음"):
            #     # 분류별 피드하는 코드
            #     # res.append({q: kakao.search_keyword(q, x=x, y=y, radius=radius, size=2)['documents']})
            res.extend(kakao.search_keyword(q, x=x, y=y, radius=radius, size=10)['documents'])
        # 검색된 장소들을 최단거리로 정렬
        res = sorted(res, key=lambda x: int(x['distance']))
        # query 확인용 코드 => 주변에 음식점이 없을 경우

        return jsonify(res)
