import flask
import db_session

app = flask.Flask(__name__)

def main():
    register_blueprints()
    db_session.global_init('postgres://localhost/plannit')
    app.run(debug = True)

def register_blueprints(app=app):

    from views import home_views
    from views import subject_views
    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(subject_views.blueprint)

if __name__ == '__main__':
    main() 
else:
    register_blueprints()
    db_session.global_init('postgres://localhost/plannit')
