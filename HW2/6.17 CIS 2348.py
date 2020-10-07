#take input from user
user_input = input('')

for letter in user_input:
    if letter == 'i':
        user_input = user_input.replace('i', '!')
    elif letter == 'a':
        user_input = user_input.replace('a', '@')
    elif letter == 'm':
        user_input = user_input.replace('m', 'M')
    elif letter == 'B':
        user_input = user_input.replace('B', '8')
    elif letter == 'o':
        user_input = user_input.replace('o', '.')
user_input = user_input + 'q*s'
print(user_input)



