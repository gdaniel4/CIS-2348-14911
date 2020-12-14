# Gabriel Daniels
# PSID: 1856516

# import modules
import csv
from operator import itemgetter
from collections import defaultdict
# import class date from module datetime
from datetime import datetime
# set up dictionaries and lists to be used later
item_id = {}
item_type = {}
damaged = {}
manufacturers = {}
prices = {}
dates = {}
PhoneInventory = []
TowerInventory = []
LaptopInventory = []

with open('ManufacturerList.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        item_id[row[0]] = None
        item_type[row[0]] = row[2]


with open('ManufacturerList.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        manufacturers[row[0]] = row[1].replace(' ', '')

with open('ManufacturerList.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        damaged[row[0]] = row[3]

with open('PriceList.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        prices[row[0]] = row[1]

with open('ServiceDatesList.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        dates[row[0]] = row[1]

# uses defaultdict function from collections class
masterdict = defaultdict(list)
# uses first arg as keys and remaining args as fill in data for the values
for d in (item_id, manufacturers, item_type, prices, dates, damaged):
    for key, value in d.items():
        masterdict[key].append(value)

# initialize list
ind_row = []
# convert key-value list dictionary to lists of list
for key, value in masterdict.items():
    # delete the 'None' from every list within the list
    del value[0]
    # add key and values of each lists of list to a list that mimics a row on the csv
    ind_row.append([key] + value)


with open('FullInventory.csv', 'w') as csv_out:
    csv_writer = csv.writer(csv_out, delimiter=',', lineterminator='\n')
    sort = sorted(ind_row, key=lambda row: row[1], reverse=False)
    for row in sort:
        csv_writer.writerow(row)


with open('FullInventory.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[2] == 'tower':
            TowerInventory.append(row)
            TowerInventory = sorted(TowerInventory)
        if row[2] == 'phone':
            PhoneInventory.append(row)
            PhoneInventory = sorted(PhoneInventory)
        if row[2] == 'laptop':
            LaptopInventory.append(row)
            LaptopInventory = sorted(LaptopInventory)

with open('TowerInventory.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
    for row in TowerInventory:
        del row[2]
        csv_writer.writerow(row)

with open('PhoneInventory.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
    for row in PhoneInventory:
        del row[2]
        csv_writer.writerow(row)

with open('LaptopInventory.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
    for row in LaptopInventory:
        count = 0
        del row[2]
        csv_writer.writerow(row)

# gets current date from date class
today = datetime.today()

# formats date into correct format
with open('FullInventory.csv', 'r') as csv_file, open('PastServiceDateInventory.csv', 'w') as csv_out:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_writer = csv.writer(csv_out, delimiter=',', lineterminator='\n')
    sort = sorted(csv_reader, key=lambda row: datetime.strptime(row[4], '%m/%d/%Y'), reverse=False)
    for item in sort:
        # converts date in each row inside sort into datetime in order to be compared
        date_time_date = datetime.strptime(item[4], '%m/%d/%Y')
        if date_time_date < today:
            csv_writer.writerow(item)

# created csv called 'DamagedInventory' and opens 'FullInventory' in order to get info to put in 'DamagedInventory'
with open('FullInventory.csv', 'r') as csv_file, open('DamagedInventory.csv', 'w') as csv_out:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_writer = csv.writer(csv_out, delimiter=',', lineterminator='\n')
    # sorts data from FullInventory csv by price in descending order
    sort = sorted(csv_reader, key=lambda row: int(row[3]), reverse=True)
    # for every row in the list created by the sort function
    for row in sort:
        if row[5] == 'damaged':
            # deletes the 'damaged' so the row can be written in the right format
            del row[5]
            csv_writer.writerow(row)


# function used to find the closest price
def closestprice(user_cart_price, suggest_price):
    try:
        absolute_diff = lambda suggest_price: abs(suggest_price - user_cart_price[0])
        closest_value = min(suggest_price, key=absolute_diff)
        return closest_value

    # when the man. name is entered incorrectly, it causes a val. error instead of outputting
    # no such inventory
    except ValueError:
        pass
    except TypeError:
        pass

# inputs for query
input_man = str(input('Enter your manufacturers: ')).capitalize()
input_type = str(input('Enter you item type: ')).lower()

# empty lists to be used during query
user_cart = []
suggest_list = []
suggest_price = []
user_cart_price =[]
# 'q' is the quit button
while input_man != 'q':
    for item in range(0, len(ind_row)):
        # all conditionals needed in order to get correct items from csv
        if input_man in ind_row[item] and input_type in ind_row[item]\
                and datetime.strptime(ind_row[item][4], '%m/%d/%Y') > today \
                and ind_row[item][5] != 'damaged':
            user_cart.append(ind_row[item])
            user_cart_price.append(int(ind_row[item][3]))

        # same conditionals from first if statement in while loop except for the man. input checker
        if input_man not in ind_row[item] and input_type in ind_row[item] \
                and datetime.strptime(ind_row[item][4], '%m/%d/%Y') > today \
                and ind_row[item][5] != 'damaged':
            suggest_list.append(ind_row[item])
            # makes user_cart_price an interger so that the closestprice function can still work
            user_cart_price.append(int('0'))
    print()
    if len(user_cart) != 0:
        # sorts by price so when first item is printed, it is the most expensive item
        user_cart = sorted(user_cart, key=itemgetter(3), reverse=True)
        print('Your item is: ', user_cart[0][0], user_cart[0][1], user_cart[0][2], '$' + user_cart[0][3])
        # clears the cart after information is printed so loop functions properly
        user_cart.clear()
    # makes sure that input can accept user inputs even if they are wrong in order to output
    # proper message
    elif input_man not in ind_row[item] or input_type not in ind_row[item]:
        print('No such inventory')
        print()

    suggest_list = sorted(suggest_list, key=itemgetter(3), reverse=True)
    for i in range(0, len(suggest_list)):
        suggest_price.append(int(suggest_list[i][3]))

    if len(suggest_list) != 0:
        try:
            closestprice = closestprice(user_cart_price, suggest_price)
        # when the manufacturer or item types are entered wrong or not at all
        # there are no items in user cart so the function results in a None type error
        # instead of just displaying either a suggested item or a 'No such inventory' message
        except TypeError:
            pass
    # make sure loop proceeds if suggestions are empty
    elif len(suggest_list) == 0:
        pass

    for i in range(0, len(suggest_list)):
        # ensures there are items in suggestions cart
        if user_cart != 0:
            # makes sure the suggested item price is the same as the closest price from my function in order
            # to print the right item to be suggested
            if suggest_price[i] == closestprice:
                print('You may, also, consider: ', suggest_list[i][0], suggest_list[i][1],
                      suggest_list[i][2], '$' + suggest_list[i][3])
                print()
                # clears suggestion after it is printed so loop functions properly
                suggest_list.clear()
            # stops the loop if there are no suggested items
            else:
                break

    # queries user again after initial query
    input_man = str(input('Enter your manufacturers, or q to quit: ')).capitalize()
    # stops loop if 'q' is entered
    if input_man == 'Q':
        break
    # ensures loop continues
    else:
        pass
    input_type = str(input('Please enter you item type: ')).lower()
