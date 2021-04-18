from flask import Blueprint, request, jsonify
from flaskr import location_code_fetcher
from flaskr import weather_api
bp_food = Blueprint('food', __name__, url_prefix='/')

@bp_food.route('/api/v1/food', methods = ['GET'])
def get_foods():
    if request.method == 'GET':
        x = request.args.get('x')
        y = request.args.get('y')
        grid_x, grid_y = location_code_fetcher.mapToGrid(float(y), float(x))
        weather = weather_api.today_weather(str(grid_x), str(grid_y))

        foods = weather_api.query.get(weather)
        return jsonify(foods)