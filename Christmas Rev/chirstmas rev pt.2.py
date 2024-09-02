# # 1
# num = int(input('Enter a number: '))
# if num % 2 == 0:
#     print('This number is even!')
# else:
#     print('This number is odd!')
# 
# # 2
# age = int(input('Enter your age: '))
# if age > 18:
#     print('You are eligible to vote')
# else:
#     print('You are not eligible to vote yet')
#     
# # 3
# num1 = int(input('Enter a number: '))
# num2 = int(input('Enter a second number: '))
# if num1 > num2:
#     print(f'{num1} is the largest number!')
# elif num2 > num1:
#     print(f'{num2} is the largest number!')
    
# 4
# number = int(input('Enter a number: '))
# if number > 0:
#     print('Positive')
# elif number < 0:
#     print('Negative')
# else:
#     print('Zero')
    
# 5
# age = int(input('Enter your age: '))
# if age >= 0 and age <= 12:
#     print('Child')
# if age >= 13 and age <= 19:
#     print('Teenager')
# if age >= 20 and age <= 59:
#     print('Adult')
# if age >= 60:
#     print('Senior Citizen')
    
# 6
# n = int(input('Enter a number between 1 - 7: '))
# weekday = 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'
# print(weekday[n - 1])

# 7
# w = float(input('Enter your weight in kg: '))
# 
# h = float(input('Enter your height in meters: '))
# bmi = w / (h * h)
# if bmi < 18.5:
#     print('Underweight')
# elif bmi >= 18.5 and bmi <= 24.9:
#     print('Normal weight')
# elif bmi >= 25 and bmi <= 29.9:
#     print('Overweight')
# else:
#     print('Obesity')
    
# 8
# mark1 = int(input('Marks out of 100 in English: '))
# mark2 = int(input('Marks out of 100 in Irish: '))
# mark3 = int(input('Marks out of 100 in Maths: '))
# 
# grade = (mark1 + mark2 + mark3) / 3
# if grade >= 90:
#     print('A')
# elif grade >= 80 and grade <= 89:
#     print('B')
# elif grade >= 70 and grade <= 79 :
#     print('C')
# elif grade >= 60 and grade <= 69:
#     print('D')
# else:
#     print('F')
    
# 9
# import math as m
# 
# a = int(input('Enter the value of the coefficient of x2: '))
# b = int(input('Enter the value of the coefficient of x: '))
# c = int(input('Enter the value of the constant: '))
# eq = - b +- m.sqrt((b ** 2 - 4 * a * c) / 2 * a)
# 
# discrim = b ** 2 - 4 * a * c
# if discrim == 0:
#     roots = 'equal roots'
# elif discrim > 0:
#     roots = 'two real roots'
# elif discrim < 0:
#     roots = 'two complex roots'
# print(f'The roots are {roots}')

# 10
# num1 = int(input('Enter a number: '))
# num2 = int(input('Enter a second number: '))
# num3 = int(input('Enter a third number: '))
# if num1 < num2 and num1 < num3:
#     if num2 < num3:
#         print(num1, num2, num3)
#     else:
#         print(num1, num3, num2)
# elif num2 < num3 and num2 < num1:
#     if num1 < num3:
#         print(num2, num1, num3)
#     else:
#         (num2, num3, num1)
# else:
#     if num1 < num2:
#         print(num3, num1, num2)
#     else:
#         print(num3, num2, num1)
        
# 11 ***
# num1 = int(input('Enter a number: '))
# num2 = int(input('Enter a second number: '))
# num3 = int(input('Enter a third number: '))
#
#if num1 > num2 and num1 > num3:
#     largest = num1
# elif num2 > num1 and num2 > num3 :
#     largest = num2
# elif num3 > num1 and num3 > num2:
#     largest = num3
# print(f'The largest num is {largest}')

# 12
# l = input('Enter a letter: ')
# v = ['a', 'e', 'o', 'i', 'u']
# if l in v:
#     print(f'{l} is a vowel!')
# else:
#     print(f'{l} is a consonant!')
    
# 13
# y = int(input('Enter a year: '))
# if y % 4 == 0:
#     print(f'{y} is a leap year')
# elif y % 4 != 0:
#     print(f'{y} is not a leap year')
       
# 14


calls = int(input('Number of calls: '))
bill = 200

if calls > 200:
    rate = 0.40
    chargeable = calls - 200
    bill += chargeable * rate
    calls -= chargeable

if calls > 150 and calls <= 200:
    rate = 0.50
    chargeable = calls - 150
    bill += chargeable * rate
    calls -= chargeable

if calls > 100 and calls <= 150:
    rate = 0.60
    chargeable = calls - 100
    bill += chargeable * rate

print(f'Total bill amount is {bill}')
    
