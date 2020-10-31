# Gabriel Daniels
# PSID 1856516

# established list
listNum = []
num = input().split()

# iterates through the list and makes all numbers integers
for i in num:
    i = int(i)
    # adds all positives back to list
    if i >= 0:
        listNum.append(i)
# sorts list and print each num out one by one
listNum.sort()
for i in listNum:
    # prints out without commas or [] and puts a space in between each number
    print(i, end=' ')
