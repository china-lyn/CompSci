# 020
name = input('Enter your name: ')
print('Your name is', len(name), 'letters long!')

#021
surname = input('Enter your last name: ')
fullname = name + ' ' + surname
print(fullname, 'your full name is', len(fullname), 'letters long')

#022
name022 = input('Enter your first name in lower case: ')
surname022 = input('Enter your last name in lower case: ')
fullname022 = name022.title() + ' ' + surname022.title()
print(fullname022)

#023
nursery = input('Type in the first line of a nursery rhyme: ')
print(len(nursery))
startno = int(input('Enter a starting number: '))
endno = int(input('Enter an ending number: '))
print(nursery[startno - 1:endno])

#024
word = input('Type in any word: ')
print(word.upper())

#025
firstname = input('Enter your first name: ')
if len(firstname) < 5:
    surname025 = input('Enter your surname: ')
    fullupper = firstname.upper() + surname025.upper()
    print(fullupper)
else:
    print(firstname.lower())
