#1/usr/bin/python
#Filename:while.py

number = 23
running = True

while running:
	guess = int(raw_input('Enter an integer:'))

	if guess == number:
		print"Congratulation, you guessed it."
		running = False#loop to stop
	elif guess < number:
		print "No,it is a little higher than than"
	else:
		print "No,it is a little lower than that"
else:
	print "The while loop is over"

print "Done" 
