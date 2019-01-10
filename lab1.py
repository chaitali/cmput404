#!/usr/bin/env python

import requests
print(requests.__version__)

r = requests.get("http://www.google.com")
#print(r.status_code)
#print(r.text)
#print(dir(r))

a = requests.get("https://raw.githubusercontent.com/chaitali/cmput404/master/lab1.py")
print(a.text)

