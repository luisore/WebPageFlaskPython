from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("/index.html")

@app.route("/hola/<nombreUsuario>")
def hola(nombreUsuario):
    return render_template("hola.html",nombre=nombreUsuario)


@app.route("/usuarios", methods = ["GET"])
def usuarios():
    usuarios = [
        {"id":1, "username": "luis",
         "email": "luis@gmail.com"},
         {"id":2, "username": "pedro",
          "email": "pedro@gmail.com"}
        ]
    return jsonify(usuarios)



if __name__ == '__main__':
    app.run(host='0.0.0.0')