#!/usr/bin/python
#Filename:method.py

class Person:
	def sayHi(self):
		print "Hello, how are you?"
	@staticmethod
	def sayHi():
		print "This the static one?"

p = Person()
p.sayHi()
