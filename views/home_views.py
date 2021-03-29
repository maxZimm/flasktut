import flask
from infrastructure.view_modifier import response
from infrastructure import cookie_auth
from services import user_services

blueprint = flask.Blueprint("home", __name__, template_folder="templates")

@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    return {}

@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    user_id = cookie_auth.get_user_id_by_cookie(flask.request)
    user = user_services.get_user_by_id(user_id)    
    return {'user': user}
