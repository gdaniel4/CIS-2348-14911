import math
#getting input from user
wallh = int(input('Enter wall height (feet):''\n'))
wallw = int(input('Enter wall width (feet):''\n'))
walla = wallh * wallw
print('Wall area:', walla, 'square feet')

#finding paint needed
paint_need = float(walla / 350)
print('Paint needed: ''{:.2f}'.format(paint_need),'gallons')

#finding cans needed
cans_need = math.ceil(paint_need)
print('Cans needed:',cans_need,'can(s)')
print('')
#Calculating expense of different colors
color_cost = {'red':'$35', 'blue':'$25', 'green':'$23'}
color = input('Choose a color to paint the wall:''\n')

print('Cost of purchasing',color, 'paint:',color_cost[color])

