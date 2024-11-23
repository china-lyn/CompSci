# Question 16(a)
# Examination Number: China

from random import randint

def guess_game(max_guesses_allowed, diff):
    if diff == 'H':
        secret_number = randint(1, 100)
    else:
        secret_number = randint(1, 5)
    guess_count = 0
    user_guess = 0
    guessed = [] # list of all numbers already guessed

    while (user_guess != secret_number and max_guesses_allowed != 0):
        user_guess = int(input("Enter your guess: "))
        if user_guess in guessed:
            print('You already guessed this number!!')
        if user_guess < secret_number: # checks if users guess is smaller/larger than the secret number
            print('Sorry! Your guess was too low')
        elif user_guess > secret_number:
            print('Sorry! Your guess was too high')
        guessed.append(user_guess) # add the number to the 'guessed' list
        
        guess_count += 1 #Increase guess_count by 1
        max_guesses_allowed -= 1 # everytime user guesses it goes down
        
        if user_guess == secret_number:
            print("Congratulations! You win!")
            print(f'You took {guess_count} guesses!') # i)

print("Welcome to the guessing game!")
userchoicemax = int(input('Enter the maximum number of guesses allowed: ')) # user chooses the max guess count
difficulty = input('Enter difficulty: E(asy) or H(ard): ')
guess_game(userchoicemax, difficulty.upper())