with open('book.txt', 'r') as f:

    common = {} # dict for the words and how many times they appear
    for line in f:
        l = line.strip().split() # sorting to just get the words
        for word in l:
            if not common.get(word): # if not already in dict, add 
                common[word] = 1
            else:
                common[word] += 1 # if in dict add 1 in value
                
top = sorted(common, reverse=True, key=common.get) # list of sorted by value

print('Most Common:\n')
for w in top[:10]:
    print(f'{w}:\t{common[w]}')