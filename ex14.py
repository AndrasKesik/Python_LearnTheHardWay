# http://learnpythonthehardway.org/book/ex14.html
from sys import argv

script, user_name, harmadik = argv
prompt = '-|: '

print("Hi {}, I'm the {} script, with another argument {}.".format(user_name, script, harmadik))
print("I'd like to ask you a few questions.")
print("Do you like me {}?".format(user_name))
likes = input(prompt)

print("Where do you live {}?".format(user_name))
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said {} about liking me.
You live in {}. Not sure where that is.
And you have a {} computer. Nice.
""".format(likes, lives, computer))

print(harmadik)
