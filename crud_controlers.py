# -*- coding: utf-8 -*-

import sqlite3

# Controlers

def create_db_row(arg_name, arg_surname, arg_email,):
    conn = sqlite3.connect('addressbook.db')
    c = conn.cursor()
    c.execute("INSERT INTO addressbook (name, surname, email) VALUES ('" + arg_name + "','" + arg_surname + "','" + arg_email +"')")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    print "Added new record"

def create_note_row(arg_id, arg_note):
    conn = sqlite3.connect('addressbook.db')
    c = conn.cursor()
    c.execute("INSERT INTO notes (f_id, note) VALUES ('" + arg_id + "','" + arg_note + "')")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    print "Added new record (a Note!)"

def read_db(arg_id):
    conn = sqlite3.connect('addressbook.db')
    c = conn.cursor()
    c.execute("SELECT * FROM addressbook ORDER BY id DESC")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

def read_db_row(arg_id):
    conn = sqlite3.connect('addressbook.db')
    c = conn.cursor()
    c.execute("SELECT * FROM addressbook WHERE id=" + arg_id + "")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_user_data(arg_id):
    conn = sqlite3.connect('addressbook.db')
    c = conn.cursor()
    c.execute("SELECT * FROM addressbook WHERE id=" + arg_id + "")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows[0][1] + " " + rows[0][2] + "<br>" + rows[0][3] 

def read_notes_db(arg_r):
    conn = sqlite3.connect('addressbook.db')
    c = conn.cursor()
    c.execute("SELECT * FROM notes DESC WHERE f_id=" + arg_r + "")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    print "<big>"
    print get_user_data(arg_r)
    print "</big><br><br>"
    print "<a href='?action=add_note&id=" + arg_r + "'>Add a note</a><br><br>"
    print "<table class='table table-striped'>"
    for row in rows:
        print "<tr><td>"
        print row[2].encode('utf-8').strip()
        print "</td><td><a href='?action=note_del&id=" + str(row[0]) + "'>Delete</a></td></tr>"
    print "</table>"


def update_db_row(arg_id, arg_name, arg_surname, arg_email):
    conn = sqlite3.connect('addressbook.db')
    c = conn.cursor()
    c.execute("UPDATE addressbook SET name='" + arg_name + "', surname='" + arg_surname+ "', email='" + arg_email + "' WHERE id=" + arg_id + "")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    print "Record updated"


def delete_db_row(arg_id):
    conn = sqlite3.connect('addressbook.db')
    c = conn.cursor()
    c.execute("DELETE FROM addressbook WHERE id=" + arg_id + "")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    print "Deleted a record..."

def delete_note_row(arg_id):
    conn = sqlite3.connect('addressbook.db')
    c = conn.cursor()
    c.execute("DELETE FROM notes WHERE id=" + arg_id + "")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    print "Deleted a record..."

