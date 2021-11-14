#!/usr/bin/env python3
from flask import Flask
from file1 import app_file1
from file2 import app_file2
main_app = Flask(__name__)
main_app.register_blueprint(app_file1)
main_app.register_blueprint(app_file2)


if __name__ == "__main__":
  main_app.run(host='0.0.0.0',port=80)

