# A list is exactly what its name says, a container of things that are organized in order


the_count = [1, 2, 3, 4, 5]
fruits = ['mangos', 'coconut', 'lychees', 'banana']
change = [1, 'pennies', 2, 'nickels', 3, 'dimes']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is the count %d" % number


for fruit in fruits:
	print "This is the fruit %s" % fruit


# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it

for i in change:
	print "I got %r" % i 

# we can also build lists, first start with an empty one

elements = []

# then use the range function to do 0 to 5 counts
for i in range (0,6):
	print "Adding %d to the list" % i
	# append is a function that lists understand
	elements.append(i)
	
#The range() function only does numbers from the first to the last, not including the last.

# now we can print them out too
for i in elements:
	print "Element was %d" % i
