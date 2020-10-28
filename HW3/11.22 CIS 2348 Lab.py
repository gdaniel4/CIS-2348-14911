#get sentence and split into individual words
list = input()
from collections import Counter
for word in list.split():
    print(f"{word} {Counter(list.split())[word]}")
