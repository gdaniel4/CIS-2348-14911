# input
a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())

ans = ''

for x in range(-10, 11):
    for y in range(-10, 11):
        q = a * x + b * y - c
        w = d * x + e * y - f
        if q == w and q == 0:
            print(x, y)
            ans = 'true'
if ans != 'true':
    print('No solution')


