#when calling this file from command line, give a file: test.txt in LearnPTHW

from sys import argv
#imported aurguements. Still a lil unsure what this does. I think it helps in doing scripts.

script, input_file = argv

def print_all(f):
	print f.read()

#f. is the variable for functions when using files. It can read, seek and etc. 

def rewind(f):
	f.seek(0)
#go back to the beginning of f. and seek 0, go to the start. 
#The 0 is NOT the 0 line 

def print_a_line(line_count, f):
	print line_count, f.readline()
#defining to print a line on f

current_file = open(input_file)

#the current file will be the opened input file

#this starts the stuff you can see on command line:
print "First, let's print the whole file:\n"

print_all(current_file)
#print_all was defined to print everything it reads
#we set the current file to be the file we input

print "Now let's rewind, kind of like a tape."

rewind(current_file)

#now we are going back to the beginning, so that the "current line" is in the start.
print "Let's print three lines"
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line+1
print_a_line(current_line+1, current_file)

current_line = current_line+1
print_a_line(current_line+1, current_file)