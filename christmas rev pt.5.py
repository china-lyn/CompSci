# 1
# numbers = input('Enter a list of numbers: ')
# numlist = numbers.split(',')
# print(','.join(numlist[::2]))

# 2
# user = input('Enter a sentence: ')
# li = user.split()
# print(li[::-1])

# 3
# numbers = []
# while True:
#     number = input('Enter a number or END when finished: ')
#     if number.upper() == 'END':
#         break
#     numbers.append(int(number))
# highest = numbers[0]
# for i in numbers:
#     if i > highest:
#         highest = i
# print(f'The highest number is {highest}')
    
# 4
# s = input('Enter a list: ')
# l = s.split()
# last = l.pop(-1)
# l.insert(0, last)
# print(s)

# 5
# s = input('Enter a sentence: ')
# print(f'Number of characters: {len(s)}')
# d = input('Enter a word you wan to delete from the sentence: ')
# print(f'Number of characters: {len(d)}')
# new = s.split(d)
# print(' '.join(new))
# print(f'Number of characters: {len(new)}')

# 6
# date = input('Enter a date in form mm/dd/yyyy: ')
# months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# d = date.split('/')
# monthint = int(d[0])
# day = int(d[1])
# year = int(d[2])
# if monthint <= 12:
#     print(f'{months[monthint]} {day}, {year}')
# else:
#     print('That is not a valid date')
    
# 7
num = input('Enter a 10 digit number: ')
numli = []
for n in num:
    numli.append(n)
    if int(n) % 2 != 0:
        print(numli.index(n), sep = ',')
        
