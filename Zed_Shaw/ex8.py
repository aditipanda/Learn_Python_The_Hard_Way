formatter = "{} {} {} {}"
print(formatter.format('one', 'two', 'three', 'four'))

# double quotes work the same as single quotes in python strings
print(formatter.format("we", "are", "not", "beautiful"))

# numbers can be passed to format strings
print(formatter.format(1, 2, 3, 4))

# boolean values can be passed to format strings
print(formatter.format(True, False, True, True))

# formatter string passed to formatter string
print(formatter.format(formatter, formatter, formatter, formatter))

# different types of things passed to format string simultaneously
print(formatter.format(1, formatter, 3, 'stunning'))
