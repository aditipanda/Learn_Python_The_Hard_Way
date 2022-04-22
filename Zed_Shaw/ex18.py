def print_many(*args):
    arg1, arg2, arg3 = args
    print("Third argument: {}".format(arg3))

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")

print_many('first', 'why so much use of double quotes..!!', 'mereko kya hai lol')
print_two("Aditi", "Panda")
print_two_again("Aditi", "Panda")
print_one("Aditi")
print_none()
