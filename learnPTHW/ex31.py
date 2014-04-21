print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input(">>> ")

if door == "1":
	print "There's a huge bear here eating a cheesecake. What do you do now?"
	print "1. Take the damn cheesecake."
	print "2. Scream at the bear"
	print "3. Call Batman"

	bear =raw_input("---> ")
#the ---> is what appears on the console where the answer has to be given

	if bear == "1":
		print "The bear just ate your face off. Cocky, eh?"
	elif bear == "2":
		print "Foolishness. You just got eaten."
	elif bear == "3":
		print "Nice....Let's see how long he takes."
	else :
		print " Well, I guess doing %s is probably better. Bear runs away" % bear
#the more options there are, the more elif you should add
#each one has to have a colon

elif door == "2":
	print "You are welcomed by Chris O'Donell. But now there's Grey's Jesse Williams and Wentworth Miller. Which one do you choose?"
	print "1. Chris O'Donell"
	print "2. Grey's Jesse Williams"
	print "3. Wentworth Miller"


	boy = raw_input(">> ")

	if boy == "1":
		print "booooo! Weak Choice."
	elif boy == "2":
		print "Well obviously.... Nice choice. Man I love that man. #Bowchicawowow"
	elif boy == "3":
		print "Amen. Wish he still did movies or TV"
	else:
		print "It's not that hard of a choice. But I guess %s is ok too." % boy

else:
	print "Man you suck at making choices. Did you really have to suggest %r . Ay dios mio." % door