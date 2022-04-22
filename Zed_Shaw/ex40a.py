# dict
mystuff = {'apple' : "I AM APPLES!"}
#print(mystuff['apple'])

# module - import in cmd line and print to check
def apple():
    print("I AM APPLES!")

tangerine = "Living reflection of a dream"

# class
class MyStuff(object):
    """docstring for MyStuff."""

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES")

thing = MyStuff()
thing.apple()
print(thing.tangerine)
