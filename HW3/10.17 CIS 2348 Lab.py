# Gabriel Daniels
# PSID 1856516

#defining CLASS attributes
class ItemToPurchase:
    item_name = ''
    item_price = float()
    item_quantity = int()

    #initializeing instance of class
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, '@', '$' + str(int(self.item_price)),
              '=', '$' + str(self.item_quantity * int(self.item_price)))

if __name__ == '__main__':
    #printing string as instructed
    print('Item 1')
    #Creating an object to the class
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    #get item1 detaiils from user
    item1.item_name = input('Enter the item name:\n')
    item1.item_price = float(input('Enter the item price:\n'))
    item1.item_quantity = int(input('Enter the item quantity:\n'))

    print('\nItem 2')
    #get item2 details from user
    item2.item_name = input('Enter the item name:\n')
    item2.item_price = float(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))

    print('\nTOTAL COST')
    #call method to print the details
    item1.print_item_cost()
    item2.print_item_cost()

    #total cost
    total = (item1.item_price * item1.item_quantity)\
            + (item2.item_price * item2.item_quantity)

    print('\nTotal: $' + str(int(total)))





