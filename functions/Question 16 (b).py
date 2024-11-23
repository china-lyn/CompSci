# Question 16(b)
# Examination Number: China

from random import randint

def numguess():
    randomnum = randint(1, 100)
    userscore = 0 # initalising score
    guess = 0
    
    while True: # will run until the users guess is the secret number
        guess = int(input('Enter your guess: '))
        print(randomnum)
        if guess < randomnum: # this if loop finds the difference between users num and secret num
            difference = randomnum - guess
        elif guess > randomnum:
            difference = guess - randomnum
            
        if guess == randomnum:
            userscore += 100
            print('JACKPOT!!!! You score 100 points :)') # if user guesses correct
            break
        elif difference <= 20: # if their guess is 20 away from the secret num
            userscore += 20
            print('You score 20 points :)')
        elif difference > 30: # if the guess is MORE than 30 away
            userscore -= 30
            print('You lose 30 points :(')
        print(f'Your total score is: {userscore}') # displaying points
        print(f'Secret number is {randomnum}. You guessed {guess}. Difference is {difference}')
        again = input('Play again? (Y/N): ')
        if again.upper() != 'Y':
            print('\nGame finished')
            break # end loop 
        else:
            continue
         
numguess()