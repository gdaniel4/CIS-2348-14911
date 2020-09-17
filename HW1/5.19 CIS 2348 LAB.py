
#Gabriel Daniels
#PSID: 1856516
#Menu
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
services = {'Oil change': '$35', 'Tire rotation': '$19', 'Car wash': '$7', 'Car wax': '$12'}
#user input
print('')
firstserv = input("Select first service:"'\n')
secondserv= input("Select second service:"'\n')
print('')
print("Davy's auto shop invoice")
print('')
#no service implementation
if firstserv == '-':
    firstserv1 = 'No service'
    print("Service 1:", firstserv1)
else:
    print("Service 1:", firstserv +',', services[firstserv])

if secondserv == '-':
    secondserv1 = 'No service'
    print("Service 2:", secondserv1)
else:
    print("Service 2:", secondserv +',',services[secondserv])
print('')

#getting rid of the dollar sign so i can convert values to interger and therfore add
value1 = services[firstserv]
if '$' in value1:
    'value1'.replace('$','')

value2 = services[secondserv]
if '$' in value2:
    'value2'.replace('$','')

print('Total: $')


#invoice

