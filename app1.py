from flask import Flask, Response

app = Flask(__name__)

@app.route("/hola")
def hola():
    return Response("HOLA DESDE API PYTHON", mimetype='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)