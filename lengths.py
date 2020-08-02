#!/usr/local/bin/python3

from cgitb import enable
enable()

from cgi import FieldStorage

print('Content-Type: text/html')
print()

form_data = FieldStorage()
length = float(form_data.getfirst('length'))
units = form_data.getfirst('units')

if units == 'inches':
    inches = length
    feet = length / 12
    yards = length / 36

elif units == 'feet':
    inches = length * 12
    feet = length
    yards = length / 3

else: 
    inches = length * 36
    feet =  length * 3
    yards = length    

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Spies</title>
        </head>
        <body>
            <table>
                <tr>
                    <th>Inches: </th><td>%.2f</td>
                </tr>
                <tr>
                    <th>Feet: </th><td>%.2f</td>
                </tr>
                <tr>
                    <th>Yards: </th><td>%.2f</td>
                </tr>
            </table>
        </body>
    </html>""" % (inches, feet, yards))
