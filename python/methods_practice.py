def birthday_print(name, date):
    print(name + "'s birthday is " + date)

names = ['Leslie','Rupesh', 'Riley']
dates = ['July 25th', 'December 1st', 'July 28th']

counter = 0
while counter < len(names):
    birthday_print(names[counter], dates[counter])
    counter = counter + 1
