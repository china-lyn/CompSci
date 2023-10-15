import random

# #052
# num = random.randint(1, 100)
# print(num)
# 
# #053
# fruit = random.choice(['raspberry','mango', 'kiwi', 'passion fruit', 'blueberry'])
# print(fruit)
# 
# #054
# choice = random.choice('ht')
# mychoice = input('Pick "h" for heads or "t" for tails: ')
# if mychoice == choice:
#     print('You win!')
# else:
#     print('Bad luck :(')
# print('The computer selected', choice)

#055
# no = random.randint(1,5)
# userno = int(input('Choose a number betweeen 1 and 5: '))
# if userno > no:
#     print('Too high!')
# elif userno < no:
#     print('Too low!')
# else:
#     print('Well done!')
#     exit()
# 
# userno = int(input('Guess again: '))
# 
# if userno == no:
#     print('Correct')
# else:
#     print('You lose! The number was', no)

# #056
# num = random.randint(1,10)
# usernum = ''
# while num != usernum:
#     usernum = int(input('Guess a number between 1 and 10: '))
# print('Well done, you got it!')

#058
score = 0
for x in range(5):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    ans = num1 + num2
    usernum = int(input(f'What is {num1} + {num2}?: '))
    if usernum == ans:
        print('Well done!')
        score += 1
print(f'You got {score} outta 5!')

#059
colours = ['pink','blue','purple','green','yellow',]
colour = random.choice(colours)
while True:
    usercolour = input(f'Pick a colour {colours}: ')
    if usercolour.lower() == colour:
        print('Well done, you got it!')
        break
    
    if colour == 'pink':
        print('Barbies favourite colour is: ')
    elif colour == 'blue':
        print('You are probably feeling BLUE right now: ')
    elif colour == 'purple':
        print('Blue and red makes: ')
    elif colour == 'green':
        print('I bet you are GREEN with envy: ')
    elif colour == 'yellow':
        print('The colour of the sun: ')
        
    
    

