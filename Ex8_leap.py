def Date(day, month, year):
    days_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year%4 == 0 and year%100 == 0 and year%400 == 0) or (year%4 == 0 and year%100 != 0) :
        #It's Leap Year
        days_of_months[1] = 29
    number = sum(days_of_months[:month-1]) + day
    print('It is day',number,'of year',year)
