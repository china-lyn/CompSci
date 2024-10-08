# FUNCTIONS
import math
import mycirclearea
import mathslibrary
 
# # 1
# def un(word):
#     new ='un' + word
#     return new
# 
# w = input('Enter a word: ')
# newword = un(w) # store as variable THEN print!!!!
# print(newword)
# 
# # 2
# def adds(word):
#     new = word + 's'
#     return new
# 
# w = input('Enter a word: ')
# print(adds(w))
 
# 3
# using imported function from file mycirclearea
# name of file.name of function

d = float(input('Enter the diameter of a circle: '))
print(f'The area of a circle with diameter of {d} is {round(mycirclearea.circle_area(d), 3)}')
 
# 4
height = float(input('Enter the height of a rectangle: '))
width = float(input('Enter the width: '))
rarea = mathslibrary.rectangle_area(height, width)
print(f'The area of a recatngle with height of {height} and width of {width} = {rarea}')
 
# 5
print('''
1) Area of a Circle
2) Perimeter of a Circle
3) Area of a Rectangle
4) Perimeter of a Rectangle
''')
while True:
    choice = int(input('\nChoose a calculation: '))
    if choice == 1:
        d = float(input('Enter the diameter of a circle: '))
        print(f'The area of a circle with diameter of {d} is {round(mycirclearea.circle_area(d), 3)}')
    elif choice == 2:
        r = float(input('Enter the radius of a cricle: '))
        print(f'The perimeter of a circle with radius of {r} is {round(mathslibrary.peri_circ(r), 3)}')#
    elif choice == 3:
        recarea = mathslibrary.rectangle_area(float(input('Enter the height of a rectangle: ')), float(input('Enter the width: ')) )
        print(f'The area of the recatngle is {recarea}')
    elif choice == 4:
        h = float(input('Enter the height of a rectangle: '))
        w = float(input('Enter the width: '))
        rperi = mathslibrary.peri_rec(h, w)
        print(f'The perimeter of a recatngle with height of {h} and width of {w} = {rperi}')
    else:
        print('That is not a valid input')
        
