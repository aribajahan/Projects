#this one should be like the script with argv, but *args is for functions
#the * in args tells python to take all the arguments to the function and then put them in args as a list.



def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
#this wil ltake 2 arguements- 2 words to print



#####
#Another way of doing the same thing
def print_two_again(arg1, arg2):
	print "arg1:%r, arg2:%r" % (arg1, arg2)
#this wil ltake 2 arguements- 2 words to print

####
def print_one(arg1):
	print "arg1: %r" % arg1
#This one won't take any arguement

def print_none ():
	print " I got nothing"


print_two("Zed", "Shaw")
#this is the arg1 and arg2
print_two_again("FUCK", "Shaw")
#this is the arg1 and arg2
print_one("First")
#this is the arg1
print_none


#in this example the argv didnt need to be imported because 
#we weren't giving the args in command line, but rather right in this file
#so in command line, we just told it to run python on this