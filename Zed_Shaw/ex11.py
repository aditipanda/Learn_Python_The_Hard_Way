# Asking Input from user

# The space is put at the end to prevent print from going to next line and ending this line with a space
print("How old are you?", end = ' ') # end is used to specify how to end the printed content
age = input()

print("How tall are you?", end = ' ')
height = input()

print("How much do you weigh?", end = ' ')
weight = input()

print(f"So you are {age} years old, are {height} inches tall, and weigh {weight} kilos.")
