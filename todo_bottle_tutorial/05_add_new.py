#!/usr/local/bin/python3

import sqlite3
from bottle import route, run,debug,template,request

DB_NAME='todo.db'

debug(True)

@route('/todo')
def todo_list():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = cur.fetchall()
    output = template('04_make_table',rows=result)

    return output

@route('/new',method='GET')
def new_item():
  new = request.GET.get('task','').strip()
  
  conn = sqlite3.connect(DB_NAME)
  cur = conn.cursor()

  if not new:
    return "Error, can not insert a blank task"

  cur.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1) )
  new_id = cur.lastrowid

  conn.commit()
  cur.close()

  return """
    <p> The new task was inserted into the database
    </p>
    <p>The new ID is %s
  """ %new_id

#note reloader param: if there is a change in file, it will reload it
run(port=8090,reloader=True)
