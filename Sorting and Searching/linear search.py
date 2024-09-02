from bubble_sort import userlist, bubblesort

# define list
l = userlist()
tnum = int(input('Enter your target number: ')) # get target num

found = False # flag

# check position of target num
for i in range(len(l)):
    if l[i] == tnum:
        print(f'The index position of your target number is {i}')
        found = True
        break

if not found:
    print('Your target number is not in this list :(') # if not in list!
