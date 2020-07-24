Year = int(input('Enter a year: '))
Month = int(input('Enter a month: '))
Day = int(input('Enter a day: '))
days_of_month = [31,28,31,30,31,30,31,31,30,31,30,31]
if (Year % 4 == 0 and Year % 100 == 0 and Year % 400 == 0) or Year % 4 == 0 and Year % 100 != 0 :
    days_of_month[1] = 29
Sum = sum(days_of_month[:Month-1]) + Day
print('this the ', [Sum], 'of the ',[Month],'of ',[Year])
