from flask import Blueprint, render_template, session,abort

app_file1 = Blueprint('app_file1',__name__)
@app_file1.route("/hello")
def hello():
    return "Hello World from app 1!"

