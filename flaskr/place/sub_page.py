from flask import Blueprint

bp1 = Blueprint('sub' , __name__, url_prefix='/sub/')

@bp1.route('index')
def second():
    return 'Second Route page!!'