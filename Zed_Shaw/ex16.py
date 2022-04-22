from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C.")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

# Opening with write mode leads to erasing file with same name,
# so truncate is not really necessary: below two lines can be commented out.
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")
# write the lines individually one by one
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# create a string to write with just one target.write()
line_to_write = line1 + "\n" + line2 + "\n" + line3 + "\n"
# print the created string
print("Here's the created string to be written into the file: ", line_to_write)
target.write(line_to_write)

print("And finally, we close it.")
target.close()

print("\nShall we read the new contents?!! Let's do it...")
print(f"Here's the new contents of the file {filename}")
target_for_reading = open(filename)
print(target_for_reading.read())
target_for_reading.close()
