import flask
from infrastructure.view_modifier import response
import db_session
from models.user import User
from services import user_services
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
            return {'errors': 'Some values are missing'}

    user = user_services.create_user(r.form['first_name'],\
                                  r.form['last_name'],\
                                  r.form['email'],\
                                  r.form['password'])
    if not user:
        return {
            'first_name': r.form['first_name'],
            'last_name': r.form['last_name'],
            'email': r.form['email'],
            'password': r.form['password'],
            'errors': 'An error occurred, user email may already be taken'
        }
    else:
        return flask.redirect('/account')
