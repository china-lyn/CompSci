l = [] # define list

# ask user to make up list
while True:
    num = input('Enter a number to add to the list, (press return to stop): ')
    if num:
        l.append(int(num))
    else:
        break
tnum = int(input('Enter your target number: ')) # get target num

# check position of target num
for i in range(len(l)):
    if l[i] == tnum:
        print(f'The index position of your target number is {i}')
    else:
        print('Your target number is not in this list :(')
