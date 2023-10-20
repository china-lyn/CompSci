#080
# name = input('Enter your first name: ')
# print(len(name))
# surname = input('Enter your surname: ')
# print(f'Your surname is {len(surname)} letters')

#081
# subject = input('Type your favourite subject: ')
# for x in subject:
#     print(x, end = '-')
    
#082
# line = 'Roses are red'
# start = int(input("'Roses are red' - pick a starting number: "))
# end = int(input("'Roses are red' - pick an ending number: "))
# print(line[start - 1:end + 1])

# #083
# while True:
#     word = input('Type in a word in uppercase: ')
#     if word != word.upper():
#         print('Try again')
#     else:
#         print('Thank you')
#         break

#084
# code = input('Enter your address: ')
# start = code[:2].upper()
# end = code[2:]
# print(start + end)

#085
# name = input('Enter your name: ')
# vowels = ['a', 'e', 'i', 'o', 'u']
# count = 0
# for x in name:
#     if x in vowels:
#         count += 1
# print(f'You have {count} vowels in your name!')
#     
#086
# p1 = input('Enter a new password: ')
# p2 = input('Enter your password again: ')
# if p1 == p2:
#     print('Thank you!')
# elif p1.lower() == p2.lower():
#     print('They must be in the same case!')
# else:
#     print('Incorrect')
#     
#086
word = input('Type in a word: ')
for x in word[::-1]:
    print(x)
    
