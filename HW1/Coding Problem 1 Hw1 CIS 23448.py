#Gabriel Daniels
#PSID: 1856516
from datetime import date
#function to get age from inputs below
def getAge(today,birthday):
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday))
    return age

#input for curent date
print('Birthday Calculator')
print('Current day')
mon = int(input('Month: '))
day = int(input('Day: '))
year = int(input('Year: '))

#input for bday
print('Birthday')
bmon = int(input('Month: '))
bday = int(input('Day: '))
byear = int(input('Year: '))
print("You are ",getAge(date(year,mon,day),date(byear,bmon,bday)),"years old.")