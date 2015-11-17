# http://learnpythonthehardway.org/book/ex11.html

print("How old are you?", end=" ")
age = input()
print("How tall are you?", end=" ")
height = input()
print("How much do you weigh?", end=" ")
weight = input()

print("Som you're {} old, {} tall and {} heavy.".format(age, height, weight))

print(input("Other question (it will print out your input immediately)? "))