import flask
from infrastructure.view_modifier import response
from infrastructure import cookie_auth
import db_session
from services import course_services, user_services

blueprint = flask.Blueprint("course", __name__, template_folder="templates")

@blueprint.route('/course/<int:course_id>', methods=['GET'])
@response(template_file='courses/course.html')
def course_get(course_id):
    user_id = cookie_auth.get_user_id_by_cookie(flask.request)
    if not user_id:
        return flask.redirect('/') 
    user = user_services.get_user_by_id(user_id)

    course = course_services.get_course_by_id(course_id)

    return {'course': course, 'user': user} 

@blueprint.route('/course/<int:course_id>/delete', methods=['POST'])
@response(template_file='courses/course.html')
def course_delete(course_id):
    d = course_services.del_course(course_id)
    print(d)
    if d:
        return flask.redirect(f'/subjects/{d}')
    else:
        return flask.redirect(f'/course/{course_id}')

@blueprint.route('/course/<int:course_id>/update', methods=['POST'])
@response(template_file='courses/course.html')
def course_update(course_id):
    r = flask.request 
    c = course_services.update_course(course_id, r.form)
    return flask.redirect(f'/course/{course_id}')
