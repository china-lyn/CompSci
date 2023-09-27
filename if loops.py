#012
num1 = input('Enter a number: ')
num2 = input('Enter a second number: ')
if num1 > num2:
    print(num2)
    print(num1)
else:
    print(num1)
    print(num2)
     
#013
num = int(input('Pick a number under 20: '))
if num >= 20:
    print('Too high')
else:
    print('Thank you!')
    
#014
no = int(input('Enter a number between 10 and 20: '))
if no >= 10 and no <= 20:
    print('Thank you!')
else:
    print('Incorrect answer :(')
    
#015
colour = input('Enter your favourite colour: ')
if colour == 'red' or 'RED' or 'Red':
    print('I like red too')
else:
    print("I don't like", colour, ", I prefer red")

#016
weather = input('Is ir raining?: ')
weather.lower()
if weather == 'yes':
    wind = input('Is it windy?: ')
    wind.lower()
    if wind == 'yes':
        print('It is too windy for an umbrella ')
    else:
        print('Take an umbrella!')
else:
    print('Enjoy your day :)')
    
    
#017
age = int(input('How old are you?: '))
if age >= 18:
    print('You can vote')
elif age == 17:
    print('You can learn to drive')
elif age == 16:
    print('You can buy a lottery ticket')
else:
    print('You can go trick-or-treating')
    
    
#018
num018 = int(input('Enter a number: '))
if num018 < 10:
    print('Too low')
elif num018 < 20:
    print('Correct')
else:
    print('Too high')

#019
numbs = int(input('Pick a number between 1, 2 or 3: '))
if numbs == 1:
    print('Thank you')
elif numbs == 2:
    print('Well done')
elif numbs == 3:
    print('Correct')
else:
    print('Error message')
    