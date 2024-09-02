# getting colours
from colorama import Fore, Style

l = []
swaps = 0
comp = 0

#asks user to make up list
while True:
    num = input(f'Enter a number to add to the list, (press return to stop): ')
    if not num:
        break
    if not num.isdigit():
        print('That is not a valid entry') # tolerance for error
        continue
    l.append(int(num))


# sets up passes
for i in range(len(l) - 1):
    print(f'\nPass {i + 1}')
    for x in range(len(l)-1):

        if l[x] > l[x + 1]:
            swaps += 1
            num = f'{Fore.GREEN}{l[x]} {l[x + 1]}{Style.RESET_ALL}'  # set colours of numbers to be swapped

            # do the swap
            l[x], l[x + 1] = l[x + 1], l[x]
            print(*l[:x], num, *l[x+2:]) # incorporate the coloured swapping numbers with the rest of the list
        else:
            comp += 1
            col = Fore.RED
            num1 = f'{Fore.RED}{l[x]} {l[x + 1]}{Style.RESET_ALL}'
            print(*l[:x], num1, *l[x+2:]) # if no swap
            
print(f'Total number of swaps: {swaps}\nTotal number of comparisons: {comp}')

            
# Simplicity and intuitive use: When the user has finished entering their list they only need to hit return to end the list making it easy to understand
# Tolerance for error: If the user types something that isn't a number it isn't an issue and the program still runs