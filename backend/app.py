from flask import Flask, render_template, jsonify
from flask_cors import CORS
from middleware import PrefixMiddleware

app = Flask(__name__)
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/api/v1')
CORS(app)

@app.route("/", methods=["GET"])
def hello_world():
    return render_template("home.html")

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({
        "message": "Hello World!"
    }), 200