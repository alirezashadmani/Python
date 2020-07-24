year = int(input('Enter a year: '))
if year % 4 != 0 :
    print('not Leap Year')
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0 :
    print('Leap Year')
elif year % 4 == 0 and year % 100 == 0 :
    print('not Leap Year')
else:
     print('Leap Year')
