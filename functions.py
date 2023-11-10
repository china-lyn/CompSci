#118
# def get_number():
#     x = int(input('Enter a number: '))
#     return x
# 
# def count(n):
#     for x in range(1, n + 1):
#         print(x)
# 
# num = get_number()
# count(num)

#119
# import random
# 
# def get_range():
#     low = int(input('Pick a low number: '))
#     high = int(input('Pick a high number: '))
#     x = random.randint(low, high)
#     return x
# 
# def num():
#     print('I am thinking of a number')
#     guess = int(input('Guess the number: '))
#     return guess
# 
# def ans(answer):
#     while True:
#         guess = num()
#         if answer < guess:
#             print('Too high guess again')
#         elif answer > guess:
#             print('Too low, guess again')
#         else:
#             break
#         
#     print('Correct, you win!')
#     
# comp_num = get_range()
# ans(comp_num)

#120
# import random
# 
# def option1():
#     n1 = random.randint(5, 20)
#     n2 = random.randint(5, 20)
#     total = n1 + n2 
#     add = int(input('Add ' + str(n1) + ' and ' + str(n2) + ': '))
#     return add, total
# 
# def option2():
#     n1 = random.randint(25, 50)
#     n2 = random.randint(1, 25)
#     answer = int(input(f'What is {n1} - {n2}:  '))
#     total = n1 - n2
#     return answer, total
# 
# def check(o):
#     if o[0] == o[1]:
#         return True
#     else:
#         return False
#         
# print('1) Addition')
# print('2) Subtraction')
# choice = input('Enter 1 or 2: ')
# if choice == '1':
#     print(check(option1()))
# elif choice == '2':
#     print(check(option2()))

#121
def addname(l):
    add = input('What is the name you want to add:\n')
    l.append(add)
    
def changename(l):
    c = input('What name would you like to change:\n')
    old = l.index(c)
    l.remove(c)
    new = input('What would you like to change it to:\n')
    l.insert(old, new)

def delete(l):
    d = input('What name would you like to delete from the list:\n ')
    l.remove(d)
    
def view(l):
    print(*l, sep = ',')
    
names = []
while True:
    print('\nWhat mode would you like to select?\n')
    print('1) Add a name')
    print('2) Change a name')
    print('3) Delete a name')
    print('4) View the list')
    print('5) End program')
    choice = int(input('\nEnter: '))
    if choice == 1:
        addname(names)
    elif choice == 2:
        changename(names)
    elif choice == 3:
        delete(names)
    elif choice == 4:
        view(names)
    elif choice == 5:
        break
    else:
        print('Invalid input')
        

    
    
    
