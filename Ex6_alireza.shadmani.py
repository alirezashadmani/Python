#Problem-045
total = 0
while total <= 50:
    Num = int(input('Enter number: '))
    total += Num
    print('The total is ... ',[total])
#####################################################
#Problem-046
Num = 0
while Num > 5:
    Num = int(input('Enter number: '))
    Num += 1
    print('The last number you entered was a', [Num])
#####################################################
#Problem-047
Num1 = int(input('Enter first number: '))
Num2 = int(input('Enter first number: '))
nums = Num1+Num2
x1 ='y'
x2 = 'n'
Question = input('Do you want to add another number? ')
while Question == x1:
    Num3 = int(input('Enter third number: '))
    nums += Num3
    Question = input('Do you want to add another number? ')
    print(nums)
#####################################################
#Problem-048
NAME = []
name = input('someone you wants to invite to a party: ')
print([name],'has now been invited')
NAME.append(name)
Question = input('Do you want to invite somebody else?')
while Question == 'yes':
    name = input('someone you wants to invite to a party: ')
    Question = input('Do you want to invite somebody else?')
    NAME.append(name)
    print(NAME)
#####################################################
#Problem-049
compnum = 50
Num = int(input('Enter a number:'))
while compnum != Num:
    print('Try another number')
    Num = int(input('Enter a number:'))
    if compnum == Num:
        print('Well done, you took',[compnum],'attempts')
#####################################################
#Problem-050
Num = 0
while Num > 10 and Num < 20:
    Num1 = int(input('Enter a number between 10 and 20: '))
    Num += Num1
    if Num1 < 10:
        print('Too Low')
    elif Num1 > 20:
        print('Too High')
    else:
        print('ThankYou')
#####################################################
#Problem-051
num = 10
print('There are',num,'green bottles hanging on the wall,',
      num,'green bottles hanging on the wall, and if 1 green bottle should accidentally fall')
num = num - 1
answer = int( input('How many green bottles will be hanging on the wall? ') )
while num > 1 :
    if answer == num :
        print('There will be',num,'green bottles hanging on the wall.')
    else :
        print('No, try again')
    print('There are',num,'green bottles hanging on the wall,',
      num,'green bottles hanging on the wall, and if 1 green bottle should accidentally fall')
    num = num - 1
    answer = int( input('How many green bottles will be hanging on the wall? ') )
if answer == num :
    print('There will be',num,'green bottle hanging on the wall.')
else :
    print('No, try again')
print('There is',num,'green bottle hanging on the wall,',
      num,'green bottle hanging on the wall, and if 1 green bottle should accidentally fall')
num = num - 1
answer = int( input('How many green bottles will be hanging on the wall? ') )
print('There are no more green bottles hanging on the wall!')
