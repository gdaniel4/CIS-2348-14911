# Gabriel Daniels
# PSID 1856516

listNum = []
num = input().split()

for i in num:
    i = int(i)
    if i >= 0:
        listNum.append(i)

listNum.sort()
for i in listNum:
    print(i, end=' ')
