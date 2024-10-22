# MAP FUNCS
# 1
words = ['apple', 'banana', 'cherry']
firstletters = list(map(lambda word: word[0], words))
print(firstletters)

# 2
uppercase = list(map(lambda word: word.upper(), words))
print(uppercase)

# 3
s = [' hello ',' world ', ' python  ']
nospace = list(map(lambda word: word.strip(), s))
print(nospace)

# 4
celsius = [0, 20, 37, 100]
f = list(map(lambda num: ((num * 9/5) + 32), celsius))
print(f)