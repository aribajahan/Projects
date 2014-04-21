def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket .\n"


print "We can just give the function numbers directly:"
cheese_and_crackers (20,30)
#the function call has to be in the same format as entered when defining it.


#Output:
#We can just give the function numbers directly:
#You have 20 cheeses!
#You have 30 boxes of crackers!
#Man that's enough for a party!
#Get a blanket .

############################################################
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#notice that we are not using the same varialbe names
#this works because we still called the same script/function: cheese_and_crackers


#OUTPUT:
#OR, we can use variables from our script:
#You have 10 cheeses!
#You have 50 boxes of crackers!
#Man that's enough for a party!
#Get a blanket .


############################################################
print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)
#this works because we still called the same script/function: cheese_and_crackers
#in this case we are still using the same variables as ex 1 but placing diff numbers in it

#OUTPUT:
#We can even do math inside too:
#You have 30 cheeses!
#You have 11 boxes of crackers!
#Man that's enough for a party!
#Get a blanket .

############################################################
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers + 1000)
#Its using the number values from the 2nd ex and adding to it

#OUTPUT:
#And we can combine the two, variables and math:
#You have 110 cheeses!
#You have 1050 boxes of crackers!
#Man that's enough for a party!
#Get a blanket .

