import flask
from infrastructure.view_modifier import response

blueprint = flask.Blueprint("subject", __name__, template_folder="templates")

@blueprint.route('/subjects')
@response(template_file='subjects/subjects.html')
def subjects():
    return {}

@blueprint.route('/subjects/<subject_name>')
@response(template_file='subjects/subject.html')
def subject(subject_name):
    return {'subject_name': 'WebDev', 'details': ['Frameworks', 'Networking', 'Hosting']}
