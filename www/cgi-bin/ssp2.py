#!/usr/bin/env python
import os
print("Content-type: text/html\n")
qs = os.environ['QUERY_STRING']
if 'firstname' in qs:
    name = qs.split('=')[1]
else:
    name = 'No Name Provided'
print("<html>")
print("<body>")
print("<h1>Hello %s</h1>" % name)
print("</body>")
print("</html>")
