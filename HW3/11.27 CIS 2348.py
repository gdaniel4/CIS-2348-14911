#Create dictionary
team_dict={}

#declare index of dictionary
i=1

count=1

#use for-loop to repeat input for 6 times
for i in range(1,6):

    #prompt for the jersy number and rating
    jersey_number = int(input('Enter player {}\'s jersey number:\n' .format(i)))
    rating = int(input('Enter player {}\'s rating:\n' .format(i)))

    #print empty line
    print()

    #check for the validation of inputs
    if jersey_number < 0 and jersey_number > 99 and rating < 0 and rating > 9:
        print('invalid entry')
        break
    else:
        team_dict[jersey_number] = rating

#print the output
print("ROSTER")

for jersey_number,rating in sorted(team_dict.items()):
    print("Jersey number: %d, Rating: %d" % (jersey_number,rating))

#Declare menu option for input
option=''
#looping until user quits, your code didn't have
#a loop for continously displaying menu

while option.upper()!='Q':
    print('\nMENU\na - Add player\nd - Remove player\nu - Update player rating\n'
          'r - Output players above a rating\no - Output roster\nq - Quit\n')

    #prompt for the option
    option = input('Choose an option:\n')

    #if option is a
    if option == 'a':

        #prompt for jersy number and rating
        #add the items in the dictinary
        jersey_number = int(input('Enter a new player\'s jersey number:\n' .format(i)))
        rating = int(input('Enter the players\'s rating:\n'.format(i)))
        team_dict[jersey_number] = rating

    #if option is d
    elif option == 'd':
        #prompt for jersy number
        jersey_number = int(input('Enter a jersey number:\n'))
        if jersey_number in team_dict.keys():
            #remove the item in the dictionary
            del team_dict[jersey_number]

    #if option is u
    elif option == 'u':

        #prompt for the jersy number
        jersey_number = int(input('Enter a jersey number:\n'))
        if jersey_number in team_dict.keys():
            #prompt for the rating of the player
            rating = int(input('Enter a new rating for player:\n'))
            #update the rating
            team_dict[jersey_number] = rating

    #If option is r
    elif option == 'r':

        #prompt rating
        rating_input=int(input('Enter a rating:\n'))
        print('ABOVE {}'.format(rating_input))

        #printing all players with rating above given rating
        for jersey_number,rating in sorted(team_dict.items()):
            if rating > rating_input:
                print("Jersey number: %d, Rating: %d" % (jersey_number,rating))

    #if option is o
    elif option == 'o':
        #printing the entire Roster
        print("ROSTER")
        #print the jersy numbers along with rating
        for jersey_number,rating in sorted(team_dict.items()):
            print("Jersey number: %d, Rating: %d" % (jersey_number,rating))