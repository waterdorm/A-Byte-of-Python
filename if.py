#!/usr/bin/python
#Filename:if.py

number = 23
guess = int(raw_input('Enter an integer:'))

if guess == number:
	print"Congratulations, you guessed it."
elif guess < number:
	print "No,it a litter higher than that"
else:
	print"No,it is a little lower than that"
print "Done"



