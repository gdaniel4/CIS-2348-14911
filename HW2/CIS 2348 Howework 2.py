month_list = {'January': '1', 'February': '2','March': '3','April': '4','May': '5','June': '6','July': '7','August': '8','September': '9','October': '10','November': '11', 'December': '12'}
input_dates = open(r'C:\Users\gabed\OneDrive\Documents\Gabriel Daniels\inputDates.txt')
parsedDates = open('C:\\Users\\gabed\\OneDrive\\Documents\\Gabriel Daniels\\parsedDates.txt','w')

#reads dates from input
"""enter_date = input("Format date as Month Day, Year (January 1, 1999): ")
enter_date = enter_date.replace(',','')
enter_date = enter_date.split(' ')"""

#gets list made by .split and replaces month with interger using dictionary above
"""month = enter_date[0]
month = month_list[month]
enter_date[0] = month
#rejoins the date with all intergers to match formatting
date = '/'.join(enter_date)
print(date)"""

#Parses input dates into correct format
for date in input_dates:
    if '/' in date:
        continue
    elif '.' in date:
        continue
    elif '-' in date:
        continue
    elif date != "-1":
        # reads dates from input
        date = date.replace(',','')
        date = date.split(' ')
        # gets list made by .split and replaces month with interger using dictionary above
        month = date[0]
        month = month_list[month]
        date[0] = month
        # rejoins the date with all intergers to match formatting
        date = '/'.join(date)
        #puts all properly formatted dates into list
        parsedDates.write(date)
        print(date)

parsedDates.close()
input_dates.close()

