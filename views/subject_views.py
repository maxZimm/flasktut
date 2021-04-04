import flask
from infrastructure.view_modifier import response
import db_session
from models.subject import Subject
from infrastructure import cookie_auth
from services import user_services, subject_services

blueprint = flask.Blueprint("subject", __name__, template_folder="templates")

@blueprint.route('/subjects', methods=['GET'])
@response(template_file='subjects/subjects.html')
def subjects():
    user_id = cookie_auth.get_user_id_by_cookie(flask.request)
    if not user_id:
        return flask.redirect('/account/login')

    user = user_services.get_user_by_id(user_id)
    return {'user': user }

@blueprint.route('/subjects', methods=['POST'])
@response(template_file='subjects/subjects.html')
def subjects_post():
    user_id = cookie_auth.get_user_id_by_cookie(flask.request)
    user = user_services.get_user_by_id(user_id)
    
    r = flask.request
    s = subject_services.create_subject(r.form['name'], r.form['description'], user)

    if not s:
        return { 'errors': 'unable to save subject',
                'name': r.form['name'],
                'description': r.form['description']}
    else:
        resp = flask.redirect(f'subjects/{s.id}')
        return resp

@blueprint.route('/subjects/<int:subject_id>')
@response(template_file='subjects/subject.html')
def subject_get(subject_id):
    user_id = cookie_auth.get_user_id_by_cookie(flask.request)
    if not user_id:
        return flask.redirect('/account/login')
    subject = subject_services.get_subject_by_id(subject_id)
    return {'subject': subject}
