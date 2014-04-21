def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a + b

def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a - b


def multiply(a,b):
	print "MULTIPLYING %d * %d" % (a,b)
	return a * b

def divide(a,b):
	print "DIVIDING %d / %d" % (a,b)
	return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
#this adds 30 to 5, and prints the line that was part of the function.
height = subtract (78, 4)
#this subtracts 4 from 78 and prints the SUBTRACTING line due to the function
weight = multiply (90, 2)
#this line multiplies 90 and 2 then prints the MULTIPYLING line due to the function
iq = divide (100, 2)

#because we have defined the terms earlier, we are able to call the functions here by only giving the numbers
#the print part is part of the function, that's why it shows what is being added, subtracted, multiplied, divided


print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
#now it can print all the values since the math is done

#A puzzle for extra credit
print "Here is a puzzle."
what = add(age, subtract(height, multiply(weight,divide(iq,2))))

print "That becomes:", what, "Can you do it by hand?"


