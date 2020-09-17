#Gabriel Daniels
#PSID: 1856516
# Prompt the user for the number of cups of lemon juice, water, and agave nectar needed to make lemonade.
# Prompt the user to specify the number of servings the recipe yields. Output the ingredients and serving size
lemoncups = float(input('Enter amount of lemon juice (in cups):''\n'))
watercups = float(input('Enter amount of water (in cups):''\n'))
agavecups = float(input('Enter amount of agave nectar (in cups):''\n'))
servings = float(input('How many servings does this make?''\n'))
print('')

print('Lemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lemoncups), 'cup(s) lemon juice')
print('{:.2f}'.format(watercups), 'cup(s) water')
print('{:.2f}'.format(agavecups), 'cup(s) agave nectar')
print('')
#Asking for serving size
servings1 = float(input('How many servings would you like to make?''\n'))
print('')
lemoncups = servings1 / 3
watercups = servings1 * 2.66667
agavecups = servings1 / 2.4
print('Lemonade ingredients - yields', '{:.2f}'.format(servings1), 'servings')
print('{:.2f}'.format(lemoncups), 'cup(s) lemon juice')
print('{:.2f}'.format(watercups), 'cup(s) water')
print('{:.2f}'.format(agavecups), 'cup(s) agave nectar')
print('')

print('Lemonade ingredients - yields', '{:.2f}'.format(servings1), 'servings')
lemoncups = lemoncups / 16
watercups = watercups / 16
agavecups = agavecups / 16

print('{:.2f}'.format(lemoncups), 'gallon(s) lemon juice')
print('{:.2f}'.format(watercups), 'gallon(s) water')
print('{:.2f}'.format(agavecups), 'gallon(s) agave nectar')
