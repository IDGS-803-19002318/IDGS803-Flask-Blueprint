import flask

from Alumnos.routes import alumnos
from Directivos.routes import dire
from Maestros.routes import maestros

app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['GET'])
def home():
    return flask.jsonify({'Datos': 'Home'})


app.register_blueprint(alumnos)
app.register_blueprint(dire)
app.register_blueprint(maestros)

if __name__ == '__main__':
    app.run()
