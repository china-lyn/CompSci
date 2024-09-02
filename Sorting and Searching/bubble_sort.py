# getting colours
from colorama import Fore, Style

#asks user to make up list
def userlist():
    l = []
    while True:
        num = input(f'Enter a number to add to the list, (press return to stop): ')
        if not num:
            break
        if not num.isdigit():
            print('That is not a valid entry') # tolerance for error
            continue
        l.append(int(num))
    return l

# sets up passes
def bubblesort(l, colours=False):
    swaps = 0
    comp = 0
    for i in range(len(l) - 1):
        if colours:
            print(f'\nPass {i + 1}')
        for x in range(len(l)-1):

            if l[x] > l[x + 1]:
                swaps += 1
                num = f'{Fore.GREEN}{l[x]} {l[x + 1]}{Style.RESET_ALL}'  # set colours of numbers to be swapped

                # do the swap
                l[x], l[x + 1] = l[x + 1], l[x]
                if colours:
                    print(*l[:x], num, *l[x+2:]) # incorporate the coloured swapping numbers with the rest of the list
            else:
                comp += 1
                col = Fore.RED
                num1 = f'{Fore.RED}{l[x]} {l[x + 1]}{Style.RESET_ALL}'
                if colours:
                    print(*l[:x], num1, *l[x+2:]) # if no swap
    if colours:            
        print(f'Total number of swaps: {swaps}\nTotal number of comparisons: {comp}')
    return l

if __name__ == "__main__":
    l = userlist()
    l_sorted = bubblesort(l, colours=True)
            
# Simplicity and intuitive use: When the user has finished entering their list they only need to hit return to end the list making it easy to understand
# Tolerance for error: If the user types something that isn't a number it isn't an issue and the program still runs
