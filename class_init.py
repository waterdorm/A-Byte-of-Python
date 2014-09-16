#!/bin/src/python
#Filename:class_init.py

class Person:
	def __init__(self,name):
		self.name = name
	def sayHi(self):
		print "Hello, my name is %s" %(self.name)

p = Person("Swaroop")
p.sayHi()

