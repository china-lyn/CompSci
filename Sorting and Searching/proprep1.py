from bubble_sort import bubblesort

# Test inputs:
#	1, 2, 3, 3, 4, 5, 2
#
# Expected outputs:
# MEAN: 2.8571428571429
# MEDIAN: 3
# MODE: 2,3
# VALUES: 1, 2, 3, 4, 5  FREQUENCY: 1, 2, 2, 1, 1
# TOP 5: 5, 4, 3, 3, 2
# LAST 5: 1, 2, 2, 3, 3
 
 
# set up menu
def menu():
    menu ='''
  ---MENU---
    1) MEAN
    2) MEDIAN
    3) MODE
    4) FREQUENCY
    5) TOP 5 NUMBERS
    6) LAST 5 NUMBERS
    '''
    return menu

# get list
def list():
    l = []
    while len(l) <= 20:
        num = input('Enter a number to add to the list, (press return to stop): ')
        if not num:
            break
        if not num.isdigit():
            print('That is not a valid entry') # tolerance for error
            continue
        l.append(int(num))
    return l
    
def mean(l):
    s = 0 # sum of all nums 
    for i in l:
        s += i
    total = s / len(l) # divide by no. of nums in list
    return total

def median(l):
    sort = bubblesort(l)
    mid = len(sort) // 2
    if len(sort) % 2 == 0: # is it an even list
        return (sort[mid] + sort[mid - 1]) / 2 # mean of 2 middle values
    else:
        return sort[mid] # middle value
 
def mode(l):
    count = 0 
    for i in l:
        count = l.count(i) # count how many times number is in list
        if count > 1: # when it is more than once it becomes the final value
            final = i
    return final
 
 
def frequency(l):
    sort = bubblesort(l)
    values = [] # list of all numbers
    c = [] # list of the frequency of each number
    amnt = 1 # counter
    for n in sort:
        if n not in values:
            values.append(n) # adds number to the list
            amnt = 1 
            c.append(amnt) # adds frequency to second list
        else:
            c[values.index(n)] += 1 # adds to frequency when present 
    return values, c
        
def top(l):
    sort = bubblesort(l)
    return sort[-1:-6:-1] # start at end of list and go backwards
 
def last(l):
    sort = bubblesort(l)
    return sort[:5]

print(menu())
p = int(input('Which progam would you like to run?: '))
l = list()
if p == 1:
    print(f'The MEAN of your list is {mean(l)}')
elif p == 2:
    print(f'The MEDIAN of your list is {median(l)}')
elif p == 3:
    print(f'The MODE of your list is {mode(l)}')
elif p == 4:
    v, f = frequency(l)
    print('VALUES:\tFREQUENCY:') # printing column headers
    for i in range(len(v)):
        print(f'{v[i]}\t{f[i]}') # coloumn lists
elif p == 5:
    print(f'The TOP 5 NUMBERS of your list are {top(l)}')
elif p == 6:
    print(f'The LAST 5 NUMBERS of your list VALUES:{last(l)}')
