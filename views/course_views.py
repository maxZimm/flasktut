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
    user = user_services.get_user_by_id(user_id)
    if not user:
        return flask.redirect('/')
    course = course_services.get_course_by_id(course_id)

    return {'course': course, 'user': user} 
