import flask

app = flask.Flask(__name__)


@app.route('/')
@app.route('/list_prof/<list>')
def training(list):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'врач', 'штурман', 'пилот дронов']
    return flask.render_template('base.html', list=list, prof=professions)


if __name__ == '__main__':
    app.run(port=8080,  host='127.0.0.1')
