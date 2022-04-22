def while_fun(limit, increment):
    i = 0
    numbers = []
    print('inside while_fun now')
    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)

        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

while_fun(10, 5)
print('out of while_fun finally!')

numbers_new = []
for i in range(10):
    print(f"At the top i is {i}")
    numbers_new.append(i)

    i = i + 5
    print("Numbers now: ", numbers_new)

    print(f"At the bottom i is {i}")
