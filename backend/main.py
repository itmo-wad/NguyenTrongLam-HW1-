from distutils.log import error
from flask import Flask, render_template, request, send_from_directory, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for("profile"))

@app.route("/profile")
def profile():
    return render_template("index.html")

@app.route("/static/<path:file_path>")
def files(file_path):
    return url_for('static', filename=file_path)

app.run(host="localhost", port=5001, debug=True)