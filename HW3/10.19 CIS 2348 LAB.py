# Declare the class ItemToPurchase
class ItemToPurchase:

    # Parameter Constructor
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # Implement the method
    def print_item_cost(self):
        # print the output in a specifed format
        string = '{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price,
                                            (self.item_quantity * self.item_price))
        cost = self.item_quantity * self.item_price
        return string, cost

    # Implement the method print_item_description
    def print_item_description(self):
        string = '{}: {}'.format(self.item_name, self.item_description)
        print(string, end='\n')
        return string

# Declare the class ShoppingCart
class ShoppingCart:

    # Parameter Constructor
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    # Implement method to add item in the shopping cart
    def add_item(self, string):
        print('\nADD ITEM TO CART', end='\n')
        # prompt the name and description of item,price and Quentity
        item_name = str(input('Enter the item name:'))
        item_description = str(input('\nEnter the item description:'))
        item_price = int(input('\nEnter the item price:'))
        item_quantity = int(input('\nEnter the item quantity:\n'))

        # Append the above values in to the list
        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))
    # Implement the method to delete the item in
    # the cart
    def remove_item(self):
        print('REMOVE ITEM FROM CART', end='\n')
        # prompt the item to remove the list
        string = str(input('Enter name of item to remove:\n'))
        i = 0
        # Using for-loop to iterate every item
        for item in self.cart_items:
            # If item found delete in the list
            if (item.item_name == string):
                del self.cart_items[i]
                i += 1
                # set the flag value to true
                # break from the list
                flag = True
                break
            # Otherwiese set value to false
            else:
                flag = False
        # IF the value not found
        if (flag == False):
            # print the message
            print('Item not found in cart. Nothing removed.')

    # Implement the method modifyitem to chane the Quantity
    def modify_item(self):
        print('\nCHANGE ITEM QUANTITY', end='\n')
        # Prompt the input item
        name = str(input('Enter the item name: '))
        # Using for-loop to iterate every item
        for item in self.cart_items:
            # If item found update Quantity in the list
            if (item.item_name == name):
                quantity = int(input('Enter the new quantity: '))
                item.item_quantity = quantity
                # set the flag value to true
                # break from the list
                flag = True
                break
            # Otherwiese set value to false
            else:
                flag = False
        # IF the value not found
        if (flag == False):
            # print the message
            print('Item not found in cart. Nothing modified')

    # implement method to compute total number of items in the cart
    def get_num_items_in_cart(self):
        num_items = 0
        # Using for-loop to iterate the cart
        for item in self.cart_items:
            # ADD the Quantities
            num_items = num_items + item.item_quantity
        # return the num_Items
        return num_items

    # Implement the method
    def get_cost_of_cart(self):
        total_cost = 0
        cost = 0
        # Using for-loop to iterate the list
        # mulitply the price and Quantity
        # add value to the Total_Cost
        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)
            total_cost += cost
        # return the value
        return total_cost

    # Implement the method to print the total
    def print_total(self):
        total_cost = ShoppingCart.get_cost_of_cart()
        if (total_cost == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            ShoppingCart.output_cart()

    # Implement the method to print_descriptions
    def print_descriptions(self):
        print('\nOUTPUT ITEMS\' DESCRIPTIONS')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date), end='\n')
        print('\nItem Descriptions', end='\n')
        for item in self.cart_items:
            print('{}: {}'.format(item.item_name, item.item_description), end='\n')

    # Implement the method output_cart()
    def output_cart(self):
        new = ShoppingCart()
        print('\nOUTPUT SHOPPING CART', end='\n')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date), end='\n')
        print('Number of Items:', new.get_num_items_in_cart(), end='\n\n')
        tc = 0
        for item in self.cart_items:
            print('{} {} @ ${} = ${}'.format(item.item_name, item.item_quantity,
                                             item.item_price, (item.item_quantity * item.item_price)), end='\n')
            tc += (item.item_quantity * item.item_price)
        print('\nTotal: ${}'.format(tc), end='\n')


# Implement the method print_menu
def print_menu(ShoppingCart):
    customer_Cart = newCart
    string = ''
    # declare the string menu
    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            'i - Output items\' descriptions\n'
            'o - Output shopping cart\n'
            'q - Quit\n')
    command = ''
    # Using while loop
    # to iterate until user enters q
    while (command != 'q'):
        string = ''
        print(menu, end='\n')
        # Prompt the Command
        command = input('Choose an option:\n')
        # repeat the loop until user enters a,i,r,c,q commands
        while (command != 'a' and command != 'o' and command != 'i' and command != 'r'
               and command != 'c' and command != 'q'):
            command = input('Choose an option:\n')
        # If the input command is a
        if (command == 'a'):
            # call the method to the add elements to the cart
            customer_Cart.add_item(string)
        # If the input command is o
        if (command == 'o'):
            # call the method to the display the elements in the cart
            customer_Cart.output_cart()
        # If the input command is i
        if (command == 'i'):
            # call the method to the display the elements in the cart
            customer_Cart.print_descriptions()
        # If the input command is i
        if (command == 'r'):
            customer_Cart.remove_item()
        if (command == 'c'):
            customer_Cart.modify_item()

# Type main section of code here
# prompt and read the customers name
customer_name = str(input('Enter customer\'s name:'))

# prompt the date
current_date = str(input('\nEnter today\'s date:\n'))

# print the name and date
print('\nCustomer name:', customer_name, end='\n')
print('Today\'s date:', current_date, end='\n')
# call the class with the parameters
newCart = ShoppingCart(customer_name, current_date)

# print the details.
print_menu(newCart)















"""if __name__ == '__main__':
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

    print('\nTotal: $' + str(int(total)))"""





