#NUMBERS FILE
# f = open('Numbers.txt', 'w')
# f.write('1, 2, 3, 4, 5')
# f.close()
 
# NAMES FILE
# f = open('Names.txt', 'w') # creating file and adding values
# f.write('China\nAhmed\nTom\nRosie\nDearbh')
# f.close()
# 
# name = input('Enter a new name: ')
# 
# f = open('Names.txt', 'a') # appending new name to end of file 
# f.write(f'\n{name}')
# f.close
# 
# f = open('Names.txt', 'r') # printing full file with new name 
# for lines in f:
#     print(lines.strip())
# f.close()
 
# SUBJECT FILE
print('---MENU---')
print('1) Create a new file\n2) Display the new file\n3) Add a new item to the file')
  
while True:
    choice = input('Make a selection 1, 2, 3: ')
    if choice == '1':
        sub = input('\nEnter a school subject: ')
        f = open('Subject.txt',  'w') # write file from scratch
        f.write(sub)
        f.close()
        break
    elif choice == '2':
        f = open('Subject.txt', 'r')
        for line in f:
            print(line.strip())
        break
    elif choice == '3':
        newsub = input('\nEnter a new subject: ')
        with open('Subject.txt', 'a+') as f: # appending AND read and write
            f.write(f'\n{newsub}')
            f.seek(0)
            for line in f:
                print(line.strip())
        break
    else:
        print('That is not a valid entry!')