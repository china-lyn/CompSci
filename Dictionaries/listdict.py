# LISTS AND DICTIONARIES:
 
#096 - 099
my2Dlist = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]] # making table of rows and columns
for l in my2Dlist:
    print(l) # displays to the user
print('Select a row and a column from this table:')
row = int(input('ROW = 0, 1, 2, 3: '))
column = int(input('COLUMN = 0, 1, 2: '))
 
for r in my2Dlist: # to select from row and column
    for c in r:
        value = my2Dlist[row][column]
print(f'Your chosen value is {value}!') # prints output

userrow = int(input('\nChoose a row:\n0, 1, 2, 3: '))
print(my2Dlist[userrow]) # prints chosen row
new = int(input('Enter a new value: '))
my2Dlist[userrow].append(new) # adds new user value to the end of the chosen row
print(my2Dlist[userrow]) # new row with added value

userrow = int(input('\nChoose a row:\n0, 1, 2, 3: '))
usercol = int(input('Choose a column in that row:\n0, 1, 2: '))
print(f'\nThe value in that position is: {my2Dlist[userrow][usercol]}') # prints value in chosen column and row
choice = input('Would you like to change the value? (yes/no): ')
if choice.lower() == 'yes':
    userval = int(input('Enter a new value: '))
    my2Dlist[userrow][usercol] = userval
    print(f'Your new row is: {my2Dlist[userrow]}')
if choice.lower() == 'no':
    pass