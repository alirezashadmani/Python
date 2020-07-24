#Problem-069
T1 = ('Canada','USA','UK','Netherland','Norway')
print(T1)
countries = input('Enter one of the country from above list: ')
print(T1.index(countries))
################################################
#Problem-070
T1 = ('Canada','USA','UK','Netherland','Norway')
print(T1)
countries = input('Enter one of the country from above list: ')
print(T1.index(countries))
Num = int(input('Enter a number: '))
print(T1[Num])
################################################
#Problem-071
L1 = ['Basketball','Football']
sport = input('what is your favorite sport: ')
sport = sport.capitalize()
L1.append(sport)
L1.sort()
print(L1)
################################################
#Problem-072
school_subject = ['Math','Physics','Chemistary','Biology','Geography','History']
print(shcool_subject)
subject = input('which of these subjects you dont like? ')
school_subject.remove(subject)
print(school_subject)
################################################
#Problem-073
food1 = input('your first favorite food: ')
food2 = input('your second favorite food: ')
food3 = input('your third favorite food: ')
food4 = input('your fourth favorite food: ')
Food_Dict = {food1:'1',food2:'2',food3:'3',food4:'4'}
print(Food_Dict)
removable_food = input('which food you want to get rid of and remove it? ')
Food_Dict.pop(removable_food, 'Enter a number between 1 and 4')
List = list(Dic.values())
L = []
for i in range(len(List))
    str = List[i-1]
    L.append(str.capitalize())
L.sort()
print(L)
###############################################
#Problem-074
color_list = ['red','blue','black','purple','yellow','pink','white','green','orange','brown']
Num1 = int(input('Enter number between 0 and 4: '))
Num2 = int(input('Enter number between 5 and 9: '))
print(color_list[Num1:Num2])
###############################################
#Problem-075
three_digit_number = [100,200,300,400]
print(three_digit_number[0],three_digit_number[1],three_digit_number[2],three_digit_number[3])
Num = int(input('Enter a 3 digit number: '))
print(Num)
if Num == three_digit_number:
    print(three_digit_number.index(Num))
else:
    print('That is not in the list')
###############################################
#Problem-076
people1 = input('Enter the first names of three people you want to invite to a party: ')
people2 = input('Enter the second names of three people you want to invite to a party: ')
people3 = input('Enter the third names of three people you want to invite to a party: ')
people = [people1,people2,people3]
add_people = input('Do you want to add another people?')
if add_people == 'Yes':
    people4 = input('Enter the another names of people you want to invite to a party: ')
    people.append(people4)
    print(people)
else:
    print(people)
##############################################
#Problem-077
people1 = input('Enter the first names of three people you want to invite to a party: ')
people2 = input('Enter the second names of three people you want to invite to a party: ')
people3 = input('Enter the third names of three people you want to invite to a party: ')
people = [people1,people2,people3]
add_people = input('Do you want to add another people?')
if add_people == 'Yes':
    people4 = input('Enter the another names of people you want to invite to a party: ')
    people.append(people4)
    print(people)
else:
    print(people)

type_name = input('Type in one of the names on the list: ')
print(people.index(type_name))
Question = input('Do you still want that person to come to the party?')

if Question == 'No':
    people.remove(type_name)
    print(people)
##############################################
#Problem-078
show = ['Ellen show', 'Steve Harvey', 'Jimmy fallon', 'Top Gear']
print(show)
new_TV_program1 = input('Enter another show: ')
new_TV_program2 = int(input('Enter the position of new show: '))
show.insert(new_TV_program2, new_TV_program1)
print(show)
##############################################
#Problem-078
nums = []
Num = int(input('Enter numbers: '))

while Num: 
    Question = input('Do you still want the last number you entered saved? ')
    nums.remove(Num3)
    print(nums)

