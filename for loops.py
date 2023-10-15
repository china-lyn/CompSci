#035
name = input('Enter your name: ')
for x in [1,2,3]:
    print(name)

#036
name = input('Enter your name: ')
num = int(input('Enter a number: '))
for _ in range(num):
    print(name)
    
#037
name = input('Enter your name: ')
for x in name:
    print(x)
    
#038
name = input('Enter your name: ')
num = int(input('Choose a number: '))
for _ in range(num):
    for x in name:
        print(x)

#039
num = int(input('Enter a number between 1 and 12: '))
for x in range(12):
    print(x * num)
    
#040
num = int(input('Enter a number below 50:  '))
for x in range(50, num  1, -1):
    print(x)
    
#041
name = input('Enter your name: ')
num = int(input('Enter a number: '))
if num < 10:
    for x in range(num):
        print(name)
else:
    for x in range(3):
        print('Too high')
        
#042
total = 0
for x in range(5):
    num = int(input('Enter a number: '))
    included = input('Enter "y" if you want to include that number and "n" if you do not: ')
    if included == 'y':
        total = total + num
print('The total is', total)

#043
d = input('Do you want to count up "u" or down "d": ')
if d == 'u':
    topnum = int(input('Enter your top number: '))
    for x in range(1, topnum + 1):
        print(x)
elif d == 'd':
    num = int(input('Enter a number below 20: '))
    for x in range(20, num - 1, -1):
        print(x)
else:
    print("I don't understand")
    
#044
ppl = int(input('How many people do you want to invite to the party?: '))
if ppl < 10:
    for x in range(ppl):
        name = input('What is the name of the person: ')
        print(name, 'has been invited!')
else:
    print('Too many people :(')