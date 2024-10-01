# CSV FILES

# 111 - 114
with open('Books.csv', 'w+') as f:
    f.write('Book,Author,Year Released') # making csv file 
    f.write('\nTo Kill A Mockingbird,Harper Lee,1960')
    f.write('\nA Brief History of Time,Stephen Hawking,1988')
    f.write('\nThe Great Gatsby,F.Scott Fitzgerald,1922')
    f.write('\nThe Man Who Mistook His Wife for a Hat,Oliver Sacks,1985')
    f.write('\nPride and Prejudice,Jane Austen,1813')

title = input('Enter another book title: ') # user enters book to add to the file
author = input('Enter the author: ').strip()
released = input('Enter the year it was released: ').strip()
with open('Books.csv', 'a+') as f:
    f.write(f'\n{title},{author},{released}') # add to end of file
    f.seek(0) # return to beginning of file to print
    print()
    for l in f:
        b, a, y = l.strip().split(',') # sections out the book, author and year 
        print(f'{b:<40}{a:<18}{y:>16}') # print file with spaces 
        
add = int(input('\nHow many records do you want to add to the list?: '))
with open('Books.csv', 'a+') as f: # appending to the file
    for a in range(add): # by how many they choose to add
        book = input('Enter the book title: ').strip()
        au = input('Enter the author: ').strip()
        yr = input('Enter the year it was released: ').strip()
        f.write(f'\n{book},{au},{yr}') # adds data to file

with open('Books.csv', 'r') as f:
    author = input('Enter the name of an author: ').strip()
    bks = [] # list for all the books under the chosen author
    for l in f:
        b, a, y = l.strip().split(',') # sectioning out
        if author.title() == a: # if author found
            bks.append(b)
    if not bks:
        print('There are no books by that author in the records :)')
    else:
        print(*bks)

syear = int(input('Enter a starting year: '))
eyear = int(input('Enter an ending year: '))
with open('Books.csv', 'r') as f:
    header = f.readline()
    for l in f:
        b, a, y = l.strip().split(',')
        if syear <= int(y) and eyear >= int(y):
            print(b, y)    
