year=int(input('enter a year'))
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print('leap year')
elif year != 0:
    print('not lip year')
