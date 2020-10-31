# Gabriel Daniels
# PSID 1856516

# establishes roster dictionary
roster_dict = {}
# initializes i
i = 1
#loops until there have been 5 loops
for i in range(1, 6):
    jersey_number = int(input("Enter player {}\'s jersey number:\n" .format(i)))
    rating = int(input("Enter player {}\'s rating:\n" . format(i)))
    print()
    #if jersey number is less than 0 and greater than 99, the loop breaks and outputs message
    if 0 > jersey_number > 99 and 0 > rating > 9:

        break
    # if tests above are passed, the jersey : number pair are added to dictionary
    else:
        roster_dict[jersey_number] = rating
# prints out jersey: rating pair in correct format
print('ROSTER')
# uses .items() method to output key-value pairs for easy formatting
for jersey, rating in sorted(roster_dict.items()):
    print('Jersey number: {}, Rating: {}' .format(jersey, rating))
# option is empty list
option = ''
# when  option is not q, all the other options are viable
while option != 'q':
    print('\nMENU')
    #print menu options
    print("a - Add player\nd - Remove player\nu - Update player rating\n"
          "r - Output players above a rating\no - Output roster\nq - Quit")
    # empty space
    print()
    # option is changed to input
    option = input('Choose an option:\n')
    if option == 'o':
        print('ROSTER')
        # sorts roster_dict with the items function
        for jersey, rating in sorted(roster_dict.items()):
            # print out number and rating in format
            print('Jersey number: {}, Rating: {}'.format(jersey, rating))
    elif option == 'a':
        # gets new jersey number and rating and just adds it to dictionary
        jersey_number = int(input("Enter a new player's jersey number:\n"))
        rating = int(input("Enter the player's rating:\n"))
        roster_dict[jersey_number] = rating
    elif option == 'd':
        # deletes key-val pair using jersey number
        jersey_number = int(input('Enter a jersey number:\n'))
        del roster_dict[jersey_number]
    elif option == 'u':
        # gets jersey number
        jersey_number = int(input('Enter a jersey number:\n'))
        # checks to see if jersey number is in keys of dictionary
        if jersey_number in roster_dict.keys():
            # once key is confirmed in dictionary, rating is asked of user
            rating = int(input('Enter a new rating for player:\n'))
            # new key-value pair is updated from old key
            roster_dict[jersey_number] = rating
    elif option == 'r':
        # asks for a rating to filter outputs by
        rating_filter = int(input('Enter a rating:\n'))
        print()
        # formatting
        print('ABOVE', rating_filter)
        # loop to iterate through dictionary
        for jersey, rating in sorted(roster_dict.items()):
            # checks if current rating is higher than the filter cutoff
            if rating > rating_filter:
                # print out the rating and matching jersey name 
                print('Jersey number: {}, Rating: {}' .format(jersey, rating))








