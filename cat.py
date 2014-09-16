#!/usr/bin/python
#Filename:cat.py

import sys

def readfile(filename):
	'''Print a file to the standard output.'''
	f = file(filename)
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print line,
	f.close()
if len(sys.argv) < 2:
	print 'No action specified'
	sys.exit()

if sys.argv[1].startswith('--'):
	option = sys.argv[1][2:]
	#fetch sys.argv[1] but without first two characters
	if option == 'version':
		print 'Version 1.0'
	elif option == 'help':
		print 'help'
		sys.exit()
else:
	for filename in sys.argv[1:]:
		readfile(filename)
