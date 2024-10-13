HEADERS = 'userID,password\n' # constant of headers

def get_data():
    pg = {} # dictionary of data we already have
    with open('password.csv', 'r') as f:
        _ = f.readline().strip().split(',') # read and discard headers
        for l in f:
            ID, passw = l.strip().split(',') # userID and password
            pg[ID] = passw # defining in dict
    return pg

def save_data(data): # to change the file and add the new password
    with open('password.csv', 'w') as f:
        f.write(HEADERS)
        for key, v in data.items():
            f.write(f'{key},{v}\n')
 
def userID(newID, pg): # checks if ID exists
    if not pg.get(newID):
        return False # if it is a new ID
    else:
        print('This ID already exists!') # if it is already in the file
        return True

def createpass(npass):
    hasup = False # to check if capital letters exist
    haslow = False # boolean to check if lower case letters exist
    hasnum = False
    valid = False # checks password length is valid
    check = [] # final check if password is valid
    if len(npass) < 8: # checking if the password length is AT LEAST 8 charachters
        valid = False
    else:
        valid = True
    check.append(valid) # adding output to the final check list
    for c in npass:
        if c.isupper(): # if the charchter is uppercase
            hasup = True
        elif c.islower(): # if charachter is lowercase
            haslow = True # set boolean 
        elif c.isdigit(): # if charchter is a number
            hasnum = True
    check.append(hasup) # adding all my checks to the final list to be checked
    check.append(haslow)
    check.append(hasnum)

    for results in check: # to get final check if password is valid or invalid
        if False in check:
            return False
        else:
            return True
            
while True:
    print()
    print('---MENU---')
    print('1) Create a new User ID\n2) Change a password\n3) Display all user IDs\n4) Quit')
    choice = (input('Choose a number: '))

    pg = get_data() # putting info from file into dictionary pg 
    if choice == '1':
        while True: # if ID does already exist asks for a NEW ID
            ID = input('Enter a NEW user ID: ')
            if not userID(ID, pg): # if it doesn't exist
                break
            print()
            print()

        while True: # create a passsword for this ID
            print('\nEnter a password including:')
            print('''
            -> At least 8 charachters
            -> Uppercase letters
            -> Lowercase letters
            -> Numbers
            -> A special charachter
                ''')
            passw = input(': ')
            if createpass(passw) == False: # if it fails to meet the criteria
                print('\nInvalid pasword')
            else:
                print('\nPassword valid!')
                break
    elif choice == '2':
        while True:
            ID = input('Enter a user ID: ')
            if not userID(ID, pg):
                print(ID)
                print(pg)
                print(userID(ID, pg))
                print('That user does not exist')
                continue
            print('\nEnter a NEW password including:')
            print('''
            -> At least 8 charachters
            -> Uppercase letters
            -> Lowercase letters
            -> Numbers
            -> A special charachter
                ''')
            newpass = input(': ')
            if createpass(newpass) == False: # checking new password is valid
                print('\nInvalid pasword') 
            else:
                pg[ID] = newpass # changing password in dictionary
                print(f'New info: {pg}') # display new info 
                save_data(pg)
                break
    elif choice == '3': # printing the user IDs 
        print()
        for IDs in pg.keys():
            print(IDs)
    elif choice == '4': # quit 
        break
    else:
        print()
        print('That is not a valid entry') # allowance for error
        continue