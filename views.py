# -*- coding: utf-8 -*-

import sqlite3

class HeaderClass:
    def __str__(self):
        print "Content-type:text/html\r\n\r\n"
        with open("header.html", 'r') as fin:
            return fin.read()


class FooterClass:
    def __str__(self):
        with open("footer.html", 'r') as fin:
            return fin.read()

#  A bit of expriment class to mess with...
class WelcomeClass:
    def __init__(self, arg_file):
        self.var_file = arg_file

    def set_file(self, arg_file):
        self.var_file = arg_file

    def __str__(self):
        with open(self.var_file, 'r') as fin:
            return fin.read()


class FormClass:
    def __str__(self):
        with open("form.html", 'r') as fin:
            return fin.read()

class EditFormClass:
    def __str__(self):
        with open("editform.html", 'r') as fin:
            return fin.read()


class CountClass:
    def __str__(self):
        conn = sqlite3.connect('addressbook.db')
        c = conn.cursor()
        c.execute("SELECT Count(*) FROM addressbook")
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return str(rows[0][0])

class NotesClass:
    def __str__(self):
        conn = sqlite3.connect('addressbook.db')
        c = conn.cursor()
        c.execute("SELECT * FROM notes")
        rows = c.fetchall()
        conn.commit()
        conn.close()
#        return "hello"

def print_view_test(rows):
    print """\
<form action="index.cgi?action=update&id={3}" method="POST">
Name:<br>
<input type="text" name="name" value="{0}">
<br>
Surname:<br>
<input type="text" name="surname" value="{1}">
<br><br>
Email:<br>
<input type="text" name="email" value="{2}">
<br><br>
<input type="submit" value="Submit">
</form>
    """.format(rows[0][1], rows[0][2], rows[0][3], rows[0][0])

def add_note_form(arg_var):
    print """\
<form action='index.cgi?action=add_note_row&id={0}' method="POST">
Note:<br>
<input type="text" name="note" value="">
<br>
<br><br>
<input type="submit" value="Submit">
</form>
    """.format(arg_var)
