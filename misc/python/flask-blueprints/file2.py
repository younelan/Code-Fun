from flask import Blueprint, render_template, session,abort

app_file2 = Blueprint('app_file2',__name__)
@app_file2.route("/world")
def world():
    return "Hello World from app 2!"

