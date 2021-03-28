import flask
from infrastructure.view_modifier import response
import db_session
from models.user import User

blueprint = flask.Blueprint('user',__name__, template_folder='user')
 
@blueprint.route('/account', methods=['GET'])
@response(template_file='user/account.html')
def account_get():

    return {}

@blueprint.route('/account/register', methods=['GET'])
@response(template_file='user/register.html')
def regitser_get():

    return {}

@blueprint.route('/account/register', methods=['POST'])
@response(template_file='user/register.html')
def regitser_post():
    r = flask.request
    for x in r.form.values():
        if x == '':
            return {'errors': 'Somethings are missing'}

    else:
        return flask.redirect('/account')
