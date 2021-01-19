import flask

app = flask.Flask('ft')

@app.route('/')
def index():
    return 'Hola Mundo'

app.run()
