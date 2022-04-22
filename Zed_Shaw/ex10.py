# escape the double-quote as the whole string is enclosed in double quotes
print("I am 6'2\" tall")

# escape the single quote as the whole string is enclosed in single quotes
print('I am 6\'2" tall')

print("\n")
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Printing with three single quotes

print('''
Does this work as well?  Let's try...
Oh yes, it does!!
Another way to print whatever and however I want!!
YAAAAASSSSSSSSSSSSSSSSSSSS, x
''')

# Combining format string with escape sequence
print("""Here are some of my details:
\t* Name: {}\n\t* Relationship Status: {}
\v* Fiance Name: {}
""".format('Aditi', 'Engaged', 'Amit'))

print('\v Vertical tab prints this symbol at the beginning .. note it is there near Amit\'s name too')
