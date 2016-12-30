#!/usr/local/bin/python3

import sqlite3
from bottle import route, run,debug

debug(True)

@route('/hello')
@route('/todo')
def todo_list():
    conn = sqlite3.connect('qtodo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    return str(result)

#print("%i" % "hello")
#note reloader param: if there is a change in file, it will reload it
run(port=8090,reloader=True)
