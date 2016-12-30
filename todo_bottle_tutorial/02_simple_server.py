#!/usr/local/bin/python3

import sqlite3
from bottle import route, run

@route('/hello')
@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    return str(result)

run(port=8090)
