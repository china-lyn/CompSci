# LIST AND DICTS:

# 100 - 101
#print(f'\t   N      S      E      W')
print(f'\tN\tS\tE\tW')
# d = {'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694}, 'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612}, 'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859}, 'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}}
# for ppl, cord in d.items(): # printing table
#     #print(f'{ppl}\t{cord["N"]:^7}{cord["S"]:^7}{cord["E"]:^7}{cord["W"]:^7}')
#     print(f'{ppl}\t{cord["N"]}\t{cord["S"]}\t{cord["E"]}\t{cord["W"]}')
# 
# while True: # if name not in dict than ask again until it is 
#     name = input('\nEnter a name from dictionary: ')
#     if d.get(name.title()):
#         break
#     print('That name is not in the dictionary!')
# while True: # if region not in dict than ask again until it is 
#     region = input('Enter a region to change (N, S, E, W): ')
#     if d[name.title()].get(region.upper()):
#         break
#     print('That region is not valid!')
# sfigure = int(input(f'Enter a sales figure to replace {region.upper()}: '))
# d[name.title()][region.upper()] = sfigure # replace the item in specific region with new figure
# print(f'The sales for {name.title()} are:{d[name.title()]}') # display new information

# 102 - 104
s = {}
for x in range(4): # getting info for 4 people
    name = input('Enter a name: ')
    s[name] = {} #adding names to dictionary with dictionary as value
    age = input(f"Enter {name}'s age: ")
    s[name]['age'] = age 
    shoe = input(f"Enter {name}'s shoe size: ")
    s[name]['shoe size'] = shoe # adding age and shoe to the dictionary under the name
print()
for names in s:
    print(names)
while True:
    user = input('\nChoose a name from the above list: ')
    if s.get(user): # allowance for error
        break
    print('That name is not in the list!')

print(f"{user}'s age: {s[user]['age']} and shoe size: {s[user]['shoe size']}") # printing the dictionary under chosen name
print()
for n, info in s.items():
    print(f"Name: {n:<14}Age: {info['age']:>3}") # name and age but NOT shoe size
    
while True:
    remove = input('\nEnter the name of the person you want to remove: ')
    if s.get(remove): # if name is in the dict
        break
    print('This name is not in the list!')
s.pop(remove) # removing values under the chosen name
print()
for names, data in s.items(): # print final list
    print(f"Name: {names:<14}Age: {data['age']:<3}Shoe Size: {data['shoe size']}")