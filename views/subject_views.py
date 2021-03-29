import flask
from infrastructure.view_modifier import response
import db_session
from models.subject import Subject
from infrastructure import cookie_auth
from services import user_services
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
    session = db_session.create_session()
    subject = Subject()
    post_data = flask.request.form
    subject.name = post_data.get('name')
    subject.description = post_data.get('description')
    subject.user_id = 1
    session.add(subject)
    session.commit()
    return {'resp_content': flask.request.form }

@blueprint.route('/subjects/<subject_name>')
@response(template_file='subjects/subject.html')
def subject(subject_name):
    return {'subject_name': 'WebDev', 'details': ['Frameworks', 'Networking', 'Hosting']}
