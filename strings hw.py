# Task 2
# The statement print(pangram[:]) would dislay the full sentence from start to finish

# Task 3
# Q1: The first code would not work as the index ends at 3, would cause an error
# The second code would not work as you cannot change a letter of a string

# Q2: They are trying to change 'Mary' to 'Mark'

# Task 4
# PROGRAM 1: it would print the words as one long word together without spaces

word1 = 'Leaving'
word2 = 'Certificate'
word3 = 'Computer'
word4 = 'Science'
subjectname = word1 + word2 +word3 +word4
print(subjectname)

# PROGRAM 2: It would print 'Thefox jumps over the lazy dog!' - no space between 'The' and 'fox'
pangram = 'The quick brown fox jumps over the lazy dog!'
print(pangram[:3] + pangram[16:])

# PROGRAM 3: it would print the noun entered with an 's' on the end of the word
noun = input('Enter a singular noun: ')
print('The plural of '+noun+' is '+noun+'s')


# Task 6: 2 + 2 = 4 is displayed

# Task 7: It will print = 3, 3.14, 3 and Hi!
# It will print: 'Hi Hal. How are you?'

# Task 8: It will print 'Radius: 5, Area: 31.42'

# Task 9a:

name = 'James'
first = name[0]
last = name[-1]
mid = name[len(name) // 2]
print(first + mid + last)

# Task 9b:
name1 = 'JhonDipPeta'
midindex = len(name1) // 2
print(name1[midindex - 1: midindex + 2])

name2 = 'JaSonAy'
midindex = len(name2) // 2
print(name2[midindex - 1: midindex + 2])

# Task 9c:
s1 = 'Aunt'
s2 = 'Kelly'
midindex = len(s1) // 2
s3 = s1[:midindex] + s2 + s1[midindex:]
print(s3)

# Task 9d
s1 = 'America'
s2 = 'Japan'
midindex1 = len(s1) // 2
midindex2 = len(s2) // 2
s3 = s1[0] + s2[0] + s1[midindex1] + s2[midindex2] + s1[-1] + s2[-1]
print(s3)