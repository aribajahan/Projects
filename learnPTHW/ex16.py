from sys import argv

script, filename = argv
#this indicates that the arguement on command line this file will respond to
#so in command: 
#python ex16.py and filename

print "We're going to erase %r." % filename
#prompts to delete the filename given

print "If you don't want that, hit CTRL-C (^C)."
#exits
print "If you do want that, hit RETURN."


raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
#opens the file in write mode
#default open function is in the read mode

print "Truncating the file.  Goodbye!"
target.truncate()
#deletes the content of the file

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#writes in these lines in to the file that was truncated
#the file should look just like what was entered

print "And finally, we close it."
target.close()