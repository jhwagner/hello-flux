import os
import flask
from flask import request, jsonify

app = flask.Flask(__name__)

version = os.getenv("APP_VERSION")

@app.route("/")
def hello_world():
    return "Hello, world!"

@app.route("/version")
def version_route():
    return "version: %s" % version

app.run(host="0.0.0.0", port=8080)
