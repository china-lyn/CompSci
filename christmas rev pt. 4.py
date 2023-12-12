# # 1
# string = input('Enter a sentence: ')
# v = ['a', 'e', 'i', 'o', 'u']
# count = 0
# for x in string:
#     if x in v:
#         count += 1
# print(f'There are {count} vowels in your sentence')
# 
# # 2
# sentence = input('Enter a sentence: ')
# ucount = 0
# lcount = 0
# dcount = 0
# wcount = 0
# for x in sentence:
#     if x.isupper():
#         ucount += 1
#     elif x.islower():
#         lcount += 1
#     elif x.isdigit():
#         dcount += 1
#     elif x.isspace():
#         wcount += 1
# print(f'Number of uppercase: {ucount}')
# print(f'Number of lowercase: {lcount}')
# print(f'Number of digits: {dcount}')
# print(f'Number of whitespace: {wcount}')

# 3
# s = input('Enter a sentence: ')
# f = s[0]
# l = s[-1]
# m = s[1:-1]
# print(f'{l}{m}{f}')

# 4
# s = input('Enter a sentence: ')
# l = []
# for x in s:
#     l.insert(0,x)
# print(''.join(l))

# 5
# s = input('Enter a sentence: ')
# print(s[1:], s[0], sep='')

# # 6
# name = input('Enter your first, middle and surname: ')
# #initials = [name[0]]
# initials = f'{name[0]}.'
# for i, l in enumerate(name):
#     if l == ' ':
#         #initials.append(name[i + 1])
#         initials += f'{name[i + 1]}.'
# 
# print(initials)
# #print('.'.join(initials), end='.')

# 7
# w = input('Enter a word: ')
# if w[::-1] == w:
#     print(f'{w} is a palindrome')
# else:
#     print(f'{w} is not a palindrome')
    
# # 8
# s = 'SHIFT'
# print(s)
# for i in range(len(s)):
#     s = s[1:] + s[0]
#     print(s)
    
# 9
def checkpass(p):
    passed = True
    if len(p) < 8:
        print('Password must be at least eight characters long')
        passed = False

    hasupper = False
    haslower = False
    hasdigit = False
    for x in p:
        if x.isupper():
            hasupper = True
        elif x.islower():
            haslower = True
        elif x.isdigit():
            hasdigit = True
            
    if not haslower:
        print('Must contain at least one lowercase letter')
        passed = False
    if not hasupper:
        print('Must contain at least one uppercase letter')
        passed = False
    if not hasdigit:
        print('Must contain a digit')
        passed = False
  
    return passed

while True:
    p = input('Enter your password: ')
    if checkpass(p):
        print('Successful password!')
        break