print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
##############################

print "---------------"
print poem
print "---------------"

five = 10 - 2 + 3 -6
print "This should be five: %s" % five
#here the string fragmenter is also attached to the math formula above
#so then as %s is being replaced with "five" five gets replaced with the result of 5

##############################

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars /100
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)
#these 3 variables have to be in the order of the function- beans then jars then crates
#or else it'll say it has more jars than beans

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)
# here the formatter uses the resulting values by calling only those variables

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d jars." % secret_formula(start_point)
#here the same variables get called in order from the function. 
#this wouldnt work if the sentence was written in a different order from the function


























