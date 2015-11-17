# http://learnpythonthehardway.org/book/ex33.html

numbers = []


def function_you_can_call(end, howmuch):
    i = 0
    while i < end:
        print("At the top i is %d" % i)
        numbers.append(i)
        i = i + howmuch
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

function_you_can_call(6,1)

print("The numbers: ")

for num in numbers:
    print(num)