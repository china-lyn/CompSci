def isbn(s):
#     l = []
#     for c in s:
#         l = l.append(c)
#     remove = del l[-1]
#     prefix = l.insert(0, '978-')
#     
    
    nns = ''
    even = 0
    odd = 0
    total = 0
    ns = s[:-2]
    prefix = '978-' + ns
    for x in ns:
        if x.isdigit() == True:
            nns += x
    for i in range(len(nns)):
        if i % 2 == 0:
            even += i * 1
        else:
            odd = i * 3
        
    total += even + odd
        
    check = 0
    nt = total % 10
    if nt != 0:
        check = 10 - nt
    result = prefix + '-' + str(check)
    return result
        
    
n = input('Enter an ISBN number: ')
print(isbn(n))
    
    
    
        
    