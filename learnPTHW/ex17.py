from sys import argv
from os.path import exists
#This returns true if the file exists
#first file name given is the one copied from 

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()
#opens and reads the content of the file
#setting a variable to the open version because thats what we are executing on
#sets what is being read as indata so that it can be written

print "The input file is %d bytes long" % len(indata)
#lets us know how much we are about to copy and paste in to other file

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
#lets us pick if we want to continue or not

out_file = open(to_file, 'w')
out_file.write(indata)
#Opens the other file in write mode
#then writes the indata that was set earlier

print "Alright, all done"
out_file.close()
in_file.close()

#closes both files
