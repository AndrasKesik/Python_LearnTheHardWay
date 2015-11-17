 # http://learnpythonthehardway.org/book/ex19.html

# this is a function definition with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print the first parameter in some string
    print("You have {} cheeses!".format(cheese_count))
    # print the second parameter in some string
    print("You have {} boxes of crackers!".format(boxes_of_crackers))
    # print string
    print("Man that's enough for a party!")
    # print string
    print("Get a blanket.\n")
# print string
print("We can just give the function numbers directly:")
# function call with two arguments
cheese_and_crackers(20, 30)

# print string
print("OR, we can use variables fromm our script:")
# assign value to a variable
amount_of_cheese = 10
# assign value to a variable
amount_of_crackers = 50
# function call with the parameters defined above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# print string
print("We can even do math inside too:")
# function call with two evaluated parameters
cheese_and_crackers(10 + 20, 5 + 6)
# print string
print("And we can combine the two, variables and math:")
# function call with two evaluated parameters
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# my function defined with no arguments
def my_own_func():
    return True

# 10 ways of function call
my_own_func()
print(my_own_func())
input(my_own_func())
x = my_own_func()
if my_own_func() == True:
    pass
"{}".format(my_own_func())
my_own_func(my_own_func())
my_own_func(my_own_func(my_own_func()))
while my_own_func():
    break
for i in range(2):
    my_own_func()
