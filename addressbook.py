#!/usr/local/bin/python
# -*- coding: utf-8 -*-


import sqlite3
import os
import sys
import json
# import re
from cgi import parse_qs, escape, FieldStorage
import crud_controlers
import views

form = FieldStorage()
query = parse_qs(os.environ[ "QUERY_STRING" ])

#  (_Always_ escape user input to avoid script injection)
query_string_id = escape(query.get('id', [''])[0])
query_string_action = escape(query.get('action', [''])[0])
query_string_query = escape(query.get('query', [''])[0])


#  Classes that I use for returning data
obj_header_file = views.HeaderClass()
obj_footer_file = views.FooterClass()
obj_form_file = views.FormClass()
obj_welcome_file = views.WelcomeClass("form.html") # Expriment here
obj_welcome_file.set_file("form_search.html") # Set Class variable to welcome.html
obj_count = views.CountClass()
obj_edit_form = views.EditFormClass()
obj_notes = views.NotesClass()

if query_string_action == "page_add":
    print obj_header_file
    print obj_form_file
    print obj_footer_file

# JSON
elif query_string_action == "search_query":
    conn = sqlite3.connect('addressbook.db')
    c = conn.cursor()
    c.execute("SELECT * from addressbook WHERE name like '%" + query_string_query + "%' OR surname like '%" + query_string_query + "%' ")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    body = json.dumps(rows)
    print "Status: 200 OK"
    print "Content-Type: application/json"
    print "Length:", len(body)
    print ""
    print body

elif query_string_action == "search":
    print obj_header_file
    print obj_welcome_File
    print obj_footer_file

elif query_string_action == "count":
    print "Content-type:text/html\r\n\r\n"
    print obj_count

elif query_string_action == "page_list":
    print obj_header_file
    rows = crud_controlers.read_db("addressbook")
    print "<table class='table table-striped'>"
    for row in rows:
        print "<tr><td><a href='?id=" + str(row[0]) + "&action=notes'>"
        print row[1], row[2], "(" + row[3] + ")</a></td>"
        print "<td><a href='?id=" + str(row[0]) + "&action=edit'>Edit</a></td>"
        print "<td><a href='?id=" + str(row[0]) + "&action=notes'>Notes</a></td>"
        print "</tr>"
    print "</table>"
    print obj_footer_file

elif query_string_action == "edit":
    print obj_header_file
    rows = crud_controlers.read_db_row(query_string_id)
    views.print_view_test(rows)
    print "<a href='?action=delete&id=" + query_string_id + "'>Delete</a>"
    print obj_footer_file

elif query_string_action == "update":
    print obj_header_file
    crud_controlers.update_db_row(query_string_id, form.getvalue("name"), form.getvalue("surname"), form.getvalue("email"))
    print obj_footer_file

elif query_string_action == "add":
    print obj_header_file
    if form.getvalue("name") and \
    form.getvalue("surname") and \
    form.getvalue("email") is not None:
        crud_controlers.create_db_row(form.getvalue("name"), form.getvalue("surname"), form.getvalue("email"))
    else:
        print "Missing fields..."

elif query_string_action == "delete":
    print obj_header_file
    crud_controlers.delete_db_row(query_string_id)

elif query_string_action == "note_del":
    print obj_header_file
    crud_controlers.delete_note_row(query_string_id)

elif query_string_action == "notes":
    print obj_header_file
    crud_controlers.read_notes_db(query_string_id)

elif query_string_action == "add_note":
    print obj_header_file
    views.add_note_form(query_string_id)

elif query_string_action == "add_note_row":
    print obj_header_file
    crud_controlers.create_note_row(query_string_id, form.getvalue("note"))

else:
    print obj_header_file
    print obj_welcome_file
    print obj_footer_file
