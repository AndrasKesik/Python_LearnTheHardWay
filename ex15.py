# http://learnpythonthehardway.org/book/ex15.html

#imports from sys module
from sys import argv
# stores the command line arguments in 2 variables, unpacks the tuple
script, filename = argv
# opens the file, the file name was in 'filename' variable, and stores the object in a variable
txt = open(filename)
# prints out the file's name
print("Here's your file {}:".format(filename))
# prints out what is in the file
print(txt.read())
# prints out an unnecessary string what could be in the next input
print("Type the filename again:")
# prints out > and stores the input in file_again variable
file_again = input("> ")
# opens the file in file_again and stoes the object in txt_again variable
txt_again = open(file_again)
# prints what's in the file, thats name stored in the text_again variable
print(txt_again.read())
# closes file in the txt variable
txt.close()
# closes the txt_again
txt_again.close()