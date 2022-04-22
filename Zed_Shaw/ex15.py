from sys import argv

script, filename = argv

# open function returns a file
txt = open(filename)

print(f"Here's your file {filename}:")
# read function reads out the contents of the file
# here, read function has not been given any parameters
print(txt.read())

print("Type the filename again:")
file_again = input('>')

txt_again = open(file_again)
print(txt_again.read())

txt.close()
txt_again.close()
