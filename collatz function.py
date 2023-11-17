l = []
def collatz(number):
    if number % 2 == 0 :
        num = number // 2
    else:
        num = 3 * number + 1
    return num

user = int(input('Enter a number: '))
while user != 1:
    #l.append(user)
    user = collatz(user)
    print(user)
#print(l)