#045
total = 0
while total <= 50:
    num = int(input('Enter a number: '))
    total = num + total 
    print('The total is', total)
    
    
#046
usernum = int(input('Enter a number: '))
while usernum < 5:
    usernum = int(input('Enter a number: '))
    if usernum > 5:
        break
print('The last number you entered was a', usernum)

#047
num1 = int(input('Enter a number: '))
num2 = int(input('Enter a second number: '))
num_ = input('Do you want to enter another number?: ')
while num_.lower() == 'yes':
    num3 = int(input('Enter another number: '))
    total12 = num1 + num2 + num3
    num_ = input('Do you want to enter another number?: ')
    if num_.lower() == 'no':
        break
print('The total is', total12)
#048
namecount = 0
name = input('Give me the name of somebody you want to invite to a party: ')
print(name.title(),'has now been invited')
namecount = namecount + 1
invite = input('Do you want to invite someone else?: ')
while invite.lower() == 'yes':
    name = input('Give me the name of somebody else you want to invite to a party: ')
    print(name.title(),'has now been invited')
    namecount = namecount + 1
    invite = input('Do you want to invite someone else?: ')
    if invite.lower() == 'no':
        break
print(namecount, 'people are coming to the party!')

# #049
compnum = 50
number = int(input('Guess a number: '))
guess = 0
while number != compnum:
    if number < compnum:
        print('Your number is too low!')
    else:
        print('Your number is too high!')
    number = int(input('Guess again: ')) #*****
    guess = guess + 1
print('Well done, you took', guess, 'attempts!')


#050
numb = int(input('Enter a number between 10 and 20: '))
while numb < 10 or numb > 20:
    if numb < 10:
        print('Too low :(')
    else:
        print('Too high!')
    numb = int(input('Try again: '))
print('Thank you :)')


#051
bottle = 10
while bottle != 0:
    print('There are', bottle, 'green bottles hanging on the wall and if 1 green bottle should accidentally fall,')
    bottle = bottle - 1
    many = int(input('how many bottles green bottles will be hanging on the wall?: '))
    if many == bottle:
        print('There will be', bottle, 'green bottles hanging on the wall!')
    else:
        many2 = int(input('No, try again: '))
print('There are no more green bottles hanging on the wall')
    
    
