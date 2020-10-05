#reads dates from input
month_list = {'January': '1', 'February': '2','March': '3','April': '4','May': '5','June': '6','July': '7','August': '8','September': '9','October': '10','November': '11', 'December': '12'}
enter_date = input("Format date as Month Day, Year: ")
enter_date = enter_date.replace(',','')
enter_date = enter_date.split(' ')

month = enter_date[0]
month = month_list[month]
enter_date[0] = month
date = '/'.join(enter_date)
print(date)

"""month = enter_date.find("January")
date = month_list['']
print(date)
#ext_date = date.find("")"""