#!/usr/bin/python
#Filename:using_file.py

poem = '''\
	Programming is fum when the work is done
	if you want make your work also fun:
			use Python!
'''

f = file('poem.txt','w')#opem for writing
f.write(poem)#write text to file
f.close()#close the file

f = file('poem.txt')
#if no mode is specified, 'r'ead mode is assumed by default

while True:
	line = f.readline()
	if len(line) == 0:
		break
	print line,

f.close()#close the file
