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

class ShoppingCart:
    # Parameter Constructor
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, ItemToPurchase):
        item_name = str(input('Enter the item name:'))
        self.cart_items.append((ItemToPurchase(item_name)))

    def remove_item(self, string):
        string = str(input(''))
        i = 0
        #iterates through the cart_items list and find string that matches with input
        for item in self.cart_items:
            if self.cart_items[i] == string:
                # deletes matching input string from list
                self.cart_items.remove(string)
                i += 1
            else:
                print('Item not found in cart. Nothing removed.')

    # used to change the quantity of a specified item based on input
    def modify_item(self, ItemToPurchase):
        name = str(input(''))
        for item in self.cart_items:
            if item.item_name == name:
                # prompts user for new quantity
                quantity = int(input('NEW QUANTITY:'))
                item.item_quantity = quantity
            else:
                print('Item not found in cart. Nothing modified.')

    # used to get total number of items in cart
    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            #gets the quantity of current item in loop and adds it to num_items interger
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        cost = 0
        total_cost = 0
        for item in self.cart_items:
            cost = item.item_quantity * item.item_price
            total_cost += cost
        return total_cost

    def print_total(self):
        total = 0
        for item in self.cart_items:
            print(item.item_name, item.item_quantity, '@', item.item_price,
                  '=' '$' + str(item.item_quantity * item.item_price))
            total += (item.item_quantity * item.item_price)
        return total

    def print_description(self):
        for item in self.cart_items:
            description = item.item_description
            print(description)

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

    def print_menu(newCart):
        customer_Cart = newCart
        menu = ('\nMENU\n'
                'a - Add item to cart\n'
                'r - Remove item from the cart\n'
                'c - Change item quantity\n'
                "i - Output item's descriptions\n"
                'o - Output shopping cart\n'
                'q - Quit\n')

        command = ''
        while (command != 'q'):
            print(menu)
            command = input('Choose an option:')
            while (
                    command != 'a' and command != 'o' and command != 'i' and command != 'q' and command != 'r' and command != 'c'):
                command = input('Choose an option:\n')
            if (command == 'a'):
                print("\nADD ITEM TO CART")
                item_name = input('Enter the item name:\n')
                item_description = input('Enter the item description:\n')
                item_price = int(input('Enter the item price:\n'))
                item_quantity = int(input('Enter the item quantity:\n'))
                itemtoPurchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)
                customer_Cart.add_item(itemtoPurchase)
            elif (command == 'r'):
                print('REMOVE ITEM FROM CART')
                itemName = input('Enter the name of the item to remove :\n')
                customer_Cart.remove_item(itemName)
            elif (command == 'c'):
                print('\nCHANGE ITEM QUANTITY')
                itemName = input('Enter the name of the item :\n')
                quan = int(input('Enter the new quantity :\n'))
                itemToPurchase = ItemToPurchase(itemName, 0, quan)
                customer_Cart.modify_item(itemToPurchase)
            elif (command == 'o'):
                print('\nOUTPUT SHOPPING CART')
                customer_Cart.print_total()
            elif (command == 'i'):
                print('\nOUTPUT ITEMS\' DESCRIPTIONS')
                customer_Cart.print_description()



    """def print_menu(ShoppingCart):
        customer_Cart = newCart

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
                customer_Cart.modify_item()"""

if __name__ == "__main__":
   customer_name = input("Enter customer's name:\n")
   current_date = input("Enter today's date:\n")
   print("\nCustomer name: %s" %customer_name)
   print("Today's date: %s" %current_date)
   newCart = ShoppingCart(customer_name, current_date)
   newCart.print_menu(newCart)






