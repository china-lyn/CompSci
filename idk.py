sport = ['basketball', 'hockey',]
favsport = input('What is your favourite sport?: ')
sport.append(favsport)
print(sport)

subjects = ['English', 'Irish', 'Maths', 'Science', 'Art', 'History']
print(subjects)
dontlike = input('Which of these subects do you not like?:  ')
subjects.remove(dontlike)
print(subjects)

colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'pink', 'white', 'brown']
startno = int(input('Pick a starting number between 0 and 4: '))
endno = int(input('Pick an ending number between 5 and 9: '))
print(colours[startno:endno])

nums = [222, 777, 444, 888]
usernum = int(input('Enter a three digit number: '))
if usernum in nums:
    print(nums.index(usernum))
else:
    print('That number is not in the list')

