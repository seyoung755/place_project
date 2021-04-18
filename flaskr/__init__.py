import os
from flask import Flask
from flask_cors import CORS
# https 모듈 추가
import ssl

def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_object('app.config.TestingConfig')
    cors = CORS(app, resources={
        r"/v1/*": {"origin" : "*"},
        r"/api/*" : {"origin": "*"},
    })
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    # 한글 깨짐 문제
    app.config['JSON_AS_ASCII'] = False

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'


    # @app.route('/api/v1/place', methods=['POST'])
    # def search_place():
    #     temp = kakao_local_api()
    #     query = '짜장면'
    #     user = request.get_json()
    #     x = jsonify(user['x'])
    #     y = jsonify(user['y'])
    #     radius = 1000
    #
    #     return temp.search_keyword(query, x=x, y=y, radius=radius)
    #
    # @app.route('/environments/<language>')
    # def environments(language):
    #     return jsonify({"language": language})

    from . import db
    db.init_app(app)

    # from flaskr.place import place_api
    # app.register_blueprint(place_api.bp)

    from .place import place_api
    app.register_blueprint(place_api.bp)

    from .place import sub_page
    app.register_blueprint(sub_page.bp1)

    from .place import food_api
    app.register_blueprint(food_api.bp_food)
    # ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    # ssl_context.load_cert_chain(certfile='newcert.pem', keyfile='newkey.pem', password='secret')

    return app