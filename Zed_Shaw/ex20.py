from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

# No matter what line_count is, readline() reads the file line by line
def print_a_line(line_count, f):
    # end can be added to not print the new line returned by readline()
    # print fun already introduces a newline after printing so w/o end, a double \n is printed
    print(line_count, f.readline())

def print_a_line_no_lineno(f):
    print(f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

#print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Now let's print three lines one by one:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1 # this increment value could be anything,
# it does not decide the line number for readline()
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

print('Print the three lines one by one, but without line numbers...')
rewind(current_file)
print_a_line_no_lineno(current_file)
print_a_line_no_lineno(current_file)
print_a_line_no_lineno(current_file)

current_file.close()
