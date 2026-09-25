from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Aplicacion ejecutandose correctamente con Docker"


@app.route("/saludo")
def saludo():
    return "Hola desde Flask"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)