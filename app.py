import flask
import db_session
import os

app = flask.Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))

def main():
    register_blueprints()
    db_session.global_init(app.config['SQLALCHEMY_DATABASE_URI'])
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
    db_session.global_init(app.config['SQLALCHEMY_DATABASE_URI'])
