#045
total = 0
while total <= 50:
    num = int(input('Enter a number: '))
    total =+ num
    print('The total is', total)
    
    
#046
usernum = 0
while usernum < 5:
    usernum = int(input('Enter a number: '))
print('The last number you entered was a', usernum)

#047
num1 = int(input('Enter a number: '))
num2 = int(input('Enter a second number: '))
while input('Enter "y" if you want to enter another number, any other letter to continue: ') == 'y':
    num3 = int(input('Enter another number: '))
    total12 = num1 + num2 + num3
print('The total is', total12)

#048
namecount = 0
while True:
    name = input('Give me the name of somebody you want to invite to a party: ')
    print(name.title(),'has now been invited')
    namecount = namecount + 1
    invite = input('Do you want to invite someone else?: ')
    if invite.lower() == 'no':
        break
print(namecount, 'people are coming to the party!')

#049
compnum = 50
guess = 0
number = -1

while number != compnum:
    guess = guess + 1
    number = int(input('Guess a number: '))
    if number < compnum:
        print('Your number is too low!')
    elif number > compnum:
        print('Your number is too high!')
    
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
    print('\nThere are', bottle, 'green bottles hanging on the wall and if 1 green bottle should accidentally fall,')
    many = int(input('how many bottles green bottles will be hanging on the wall?: '))
    if many == bottle - 1:
        bottle = bottle - 1
        print('There will be', bottle, 'green bottles hanging on the wall!')
    else:
        print('No, try again')
print('There are no more green bottles hanging on the wall')
