# Argument variable and its unpacking
from sys import argv
script, first, second, third, fourth = argv

print("The file name is: ", script)
print("Rest variables: ", first, second, third, fourth)
print("More input?", end = ' ')
more = input();
print("Here's more:", more)
