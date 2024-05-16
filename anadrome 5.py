with open('words (1).txt', 'r') as f:

    match = []
    other = []
    for x in f:
        word = x.strip() #what
        if len(word) > 6 and word.isalpha():
            match.append(word)
    for m in match:
        if m != m[::-1] and m[::-1] in match and m[::-1] not in other:
            other.append(m)
            print(m, m[::-1])
            
            
            
            
        
        
        
# words = set()
# match = set()
# 
# with open('words (1).txt', 'r') as f:
#     for x in f:
#         word = x.strip()
#         if len(word) >= 6 and word.isalpha():
#             words.add(word)
# 
# for w in words:
#     if w != w[::-1] and w[::-1] in words and w[::-1] not in match:
#         match.add(w)
#         print(w, w[::-1])