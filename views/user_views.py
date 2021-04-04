import flask
from infrastructure.view_modifier import response
import db_session
from models.user import User
from services import user_services
from infrastructure import cookie_auth

blueprint = flask.Blueprint('user',__name__, template_folder='user')
 
@blueprint.route('/account', methods=['GET'])
@response(template_file='user/account.html')
def account_get():
    user_id = cookie_auth.get_user_id_by_cookie(flask.request)
    user = user_services.get_user_by_id(user_id)
    if not user:
        return flask.redirect('/')
    return { 'user': user }

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
        resp = flask.redirect('/account')
        cookie_auth.set_cookie(resp, user.id)
        return resp

@blueprint.route('/account/login', methods=['GET'])
@response(template_file='user/login.html')
def login_get():

    return {}

@blueprint.route('/account/login', methods=['POST'])
@response(template_file='user/login.html')
def login_post():
    r = flask.request
    for x in r.form.values():
        if x =='':
            return {'errors': 'Some values missing'}

    user = user_services.login_user(r.form['email'], r.form['password'])
    
    if not user:
        return {
            'email': r.form['email'],
            'errors': 'Email or password not recognized'
        }
    resp = flask.redirect('/account')
    cookie_auth.set_cookie(resp, user.id)
    return resp

@blueprint.route('/account/logout')
def logout():
    resp = flask.redirect('/')
    cookie_auth.logout(resp)

    return resp
