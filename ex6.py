# http://learnpythonthehardway.org/book/ex6.html

# stores the string in a variable
x = "There are {} types of people.".format(10)
# stores the string in a variable
binary = "binary"
# stores the string in a variable
do_not = "don't"
# stores the string in a variable
y = "Those who know {} and those who {}".format(binary, do_not)
# prints the x variable
print(x)
# prints the y variable
print(y)
# prints the string
print("I said: {}".format(x))
# prints the string
print("I also said: '{}'".format(y))
# stores the False bool value in the variable
hilarious = False
# stores the string in the variable
joke_evaluation = "Isn't that joke so funny?! {}"
# prints the string
print(joke_evaluation.format(hilarious))
# stores the string in a variable
w = "This is the left side of..."
# stores the string in a variable
e = "a string with a right side."
# prints the two variables as one string
print(w+e)
