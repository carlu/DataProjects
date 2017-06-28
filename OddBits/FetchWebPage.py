#!/usr/bin/python

import urllib


#page = urllib.urlopen('http://www.google.co.uk')
page = urllib.urlopen('file:///home/cu/Code/Web/startpage/index.html')

print page

Content = page.read()

print(Content)