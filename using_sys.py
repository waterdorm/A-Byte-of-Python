#!/usr/bin/python
#Filename:using_sys.py

import sys

print 'The command line argument are:'
for i in sys.argv:
	print i
print '\nThe python path is ',sys.path,'\n'
