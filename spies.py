#!/usr/local/bin/python3

from cgitb import enable
enable()

from cgi import FieldStorage

print('Content-Type: text/html')
print()

form_data = FieldStorage()
fname = form_data.getfirst('fname')
sname = form_data.getfirst('sname')

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Spies</title>
        </head>
        <body>
            <p>
                Your spy name is: %s, %s %s.
            </p>
        </body>
    </html>""" % (sname, fname, sname))
