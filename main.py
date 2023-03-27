import flask

app = flask.Flask(__name__)


@app.route('/')
@app.route('/training/<prof>')
def training(prof):
    return flask.render_template('base.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080,  host='127.0.0.1')
