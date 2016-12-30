#!/usr/local/bin/python3

import sqlite3
from bottle import route, run,debug,template

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    output = template('04_make_table',rows=result)

    return output

#note reloader param: if there is a change in file, it will reload it
run(port=8090,reloader=True)
