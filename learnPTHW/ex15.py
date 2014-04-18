from sys import argv

script, filename = argv

#this calls THIS file as the script and filename you give

txt = open(filename)
#opens the file

print "Here's your file %r:" % filename
print txt.read()
#reads and shows the text in the file

print "Type the filename again:"
file_again = raw_input(">")
#this time the file called is based on the input after the prompt

txt_again = open(file_again)

print txt_again.read()
#reads and shows the text in the file

#Command line : 
#python ex15.py ex15_sample.txt