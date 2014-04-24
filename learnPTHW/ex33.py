i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num


####################################
#here, the goal is to make it in a way where its a function

starthere = 7
#this variable has to be defined before its referred to 

def loopty (starthere): 
	i = 0
	numbers = []
	#these need to be within the definition, but outside of the while loop
	while i < starthere:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i


	print "The numbers: "

	for num in numbers:
		print num


print loopty (starthere)
#Everytime you can define a different number for starthere