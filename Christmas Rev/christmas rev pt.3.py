# 1
# for x in range(1, 11):
#     print(x)

# 2
# for x in range(20, 0, -1):
#     print(x)
    
# 3
# for x in range(2, 11,2):
#     print(x)
    
# 4
# n = int(input('Enter a number: '))
# for x in range(1, n + 1):
#     print(x)
    
# 5
# n = int(input('Enter a number: '))
# for x in range(1, n + 1, 2):
#     print(x)
    
# 6 ***
#print('Happy Birthday! ' * 5)

# 7
# n = int(input('Enter a number: '))
# l = []
# for x in range(1, n + 1):
#     sq = x ** 2
#     l.append(sq)
#     
# print(f'The first {n} terms of the series are: {" ".join(l)}')

# 8
# n = int(input('Enter a number: '))
# for i in range(1, 13):
#     a = n * i
#    print(f'{i} x {n} = {a}')

# 9
# n = -1
# l = []
# for i in range(1,9):
#     n = n + 4
#     l.append(str(n))
# print(' '.join(l))

# 10 **
# n = 2
# l = ['2']
# for i in range(1, 6):
#     n = n * 3
#     l.append(str(n))
# print(' '.join(l))

# 11 **
# num = int(input('Enter a positive number: '))
# ans = sum(range(1, num + 1))
# print(ans)

# 12
# n = int(input('Enter a positive number: '))
# l = []
# for i in range(1, n + 1):
#     i = 1 / i
#     l.append(i)
#     total = round(sum(l), 2)
# print(f'The sum of reciprocals from 1 to {n} is: {total}')

# 13
# total = 0
# for x in range(5):
#     num = int(input('Enter a number: '))
#     total += num 
# print(f'The final running total is: {total}')

# 14
# import math as m
# 
# n = int(input('Enter a positive integer: '))
# for i in range(1, n + 1):
#     f = m.factorial(i)
# print(f)

# 15
# base = int(input('Enter a base number: '))
# exp = int(input('Enter an exponent number: '))
# ans = 1
# for i in range(exp):
#     ans *= base
# print(ans)

# 16
n = int(input('How many numbers would you like to enter: '))
ans = 0
count = 0
while count < n:
    num = int(input('Enter number: '))
    if num >= 0:
        ans += num
        count += 1
    else:
        print('This is an invalid value, all numbers must be positive')
    
print(f'The sum of the {n} numbers entered is {ans}')
print(f'The average of the {n} numbers is {ans / n}')
