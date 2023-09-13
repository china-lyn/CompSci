# Task 2
# The statement print(pangram[:]) would dislay the full sentence from start to finish

# Task 3
# Q1: The first code would not work as the index ends at 3, would cause an error
# The second code would not work as you cannot change a letter of a string

# Q2: They are trying to change 'Mary' to 'Mark'

#Task 4
#PROGRAM 1: it would print the words as one long word together without spaces

word1 = 'Leaving'
word2 = 'Certificate'
word3 = 'Computer'
word4 = 'Science'
subjectname = word1 + word2 +word3 +word4
print(subjectname)

#PROGRAM 2: It would print 'Thefox jumps over the lazy dog!'
pangram = 'The quick brown fox jumps over the lazy dog!'
print(pangram[:3] + pangram[16:])