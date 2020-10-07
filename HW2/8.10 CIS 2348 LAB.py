word = input()
#remove spaces from user input
word_ = word.replace(' ', '')
#make all input lowercase so if statement can execute correctly
word_ = word_.lower()
#print word backwards
backwards_word = word_[::-1]

if word_ == backwards_word:
    print(word, 'is a palindrome')
else:
    print(word, 'is not a palindrome')