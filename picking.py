#!/usr/bin/python
#Filename:picking.py

import cPickle as p
#import pickleasp

shoplistfile = 'shoplist.data'
#the name of the file where we will store the object

shoplist = ['apple','mango','carrot']

#Write to the file
f = file(shoplistfile,'w')
p.dump(shoplist,f)
f.close()

del shoplist

#read back from the storage

f = file(shoplistfile)
storedlist = p.load(f)

print storedlist
for item in storedlist:
	print item+'\n',
