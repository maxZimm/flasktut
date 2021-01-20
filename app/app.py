import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('home/index.html')

@app.route('/about')
def about():
    return flask.render_template('home/about.html')

if __name__ == '__main__':
    app.run(debug=True)
