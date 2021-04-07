import flask
from infrastructure.view_modifier import response
import db_session
from models.subject import Subject
from infrastructure import cookie_auth
from services import user_services, subject_services, course_services

blueprint = flask.Blueprint("subject", __name__, template_folder="templates")

@blueprint.route('/subjects', methods=['GET'])
@response(template_file='subjects/subjects.html')
def subjects():
    user_id = cookie_auth.get_user_id_by_cookie(flask.request)
    if not user_id:
        return flask.redirect('/account/login')

    user = user_services.get_user_by_id(user_id)
    subjects = subject_services.get_all_subjects_user(user)
    return {'user': user , 'subjects': subjects}

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

@blueprint.route('/subjects/<int:subject_id>', methods=['GET'])
@response(template_file='subjects/subject.html')
def subject_get(subject_id):
    user_id = cookie_auth.get_user_id_by_cookie(flask.request)
    if not user_id:
        return flask.redirect('/account/login')
    user = user_services.get_user_by_id(user_id)
    subject = subject_services.get_subject_by_id(subject_id)
    courses = course_services.get_courses_by_subject(subject)
    errors = None
    return {'subject': subject, 'courses': courses, 'user': user, 'errors': errors}

@blueprint.route('/subjects/<int:subject_id>', methods=['POST'])
@response(template_file='subjects/subject.html')
def subject_post(subject_id):
    r = flask.request
    subject = subject_services.get_subject_by_id(subject_id) 
    c = course_services.create_course(r.form['name'],
                                      r.form['summary'],
                                      r.form['course_url'],
                                      subject)
    if not c:
        return {'errors': 'unable to save course',
                'name': r.form['name'],
                'summary': r.form['summary'],
                'course_url': r.form['course_url']}
    else:
        resp = flask.redirect(f'/course/{c.id}')
        return resp

@blueprint.route('/subjects/<int:subject_id>/update', methods=['POST'])
@response(template_file='subjects/subject.html')
def subject_update(subject_id):
    subject = subject_services.get_subject_by_id(subject_id)
    r = flask.request
    updated = subject_services.update_subject(subject,
                                              r.form.get('name'),
                                              r.form.get('name_prev'), 
                                              r.form.get('description'), 
                                              r.form.get('description_prev')) 
    if not updated:
        return flask.redirect(f'/subjects/{subject.id}')

    else:
        resp =  flask.redirect(f'/subjects/{subject.id}')
        return resp

@blueprint.route('/subjects/<int:subject_id>/delete', methods=['GET'])
@response(template_file='subjects/subject.html')
def subject_delete(subject_id):
    subject = subject_services.get_subject_by_id(subject_id)
    d = subject_services.del_subject(subject)
    if d:
        return flask.redirect(f'/subjects')
    else:
        return flask.redirect(f'/subjects/{subject_id}')
