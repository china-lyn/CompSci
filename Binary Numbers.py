def btod(bnum):
    dnum = 0
    power = len(bnum) - 1
    for n in bnum:
        dnum += int(n) * 2 ** power
        power -= 1
    return dnum
        
        
    
def dtob(dnum):
    bnums = []
    ans = int(dnum)
    while ans:
        remainder = ans % 2
        ans = ans // 2
        bnums.insert(0, str(remainder))
        
    return ''.join(bnums)

       
def add(b, bb):
    ans = []
    carry = 0
    max_len = max(len(b), len(bb))
    b = b.zfill(max_len)
    bb = bb.zfill(max_len)
    
    for i in range(max_len -1, -1, -1):
        res = int(b[i]) + int(b[i])
        if carry:
            res += 1
            carry = 0
        if res > 1:
            carry = 1
            if res > 2:
                res = 1
            else:
                res = 0
                
        ans.insert(0, str(res))
        if carry:
            ans.insert(0, str(carry))
    return ''.join(ans)
       
    
def htob(hexa):
    bins = []
    alpha = ('ABCDEF')
    for n in hexa:
        if n in alpha:
            n = 10 + alpha.index(n)
        b = dtob(n)
        diff = 4 - len(b)
        bins.append('0' * diff + b)
    
    return ''.join(bins).lstrip('0')
    
    
def btoh(num):
    hexa = []
    alpha = ('ABCDEF')
    end = len(num)
    print('end at start:', end)

    blocks = []
    while True:
        start = max(0, end - 4)
        block = num[start:end]
        blocks.insert(0, block)
        print(block)
        
        end -= 4
        if end < 0:
            break
        
    for block in blocks:
        h = btod(block)
        if int(h) > 9:
            print(h)
            h = alpha[h-10]
            
        hexa.append(str(h))
    
    return ''.join(hexa) 

def dtoh(dec):
    hnums = []
    d = int(dec)
    a = 'ABCDEF'
    while d != 0:
        remainder = d % 16
        if remainder > 9:
            remainder = a[remainder - 10]
        d = d // 16
        hnums.insert(0, str(remainder))
    
    return ''.join(hnums)

def htod(h):
    power = len(h) - 1
    ans = 0
    a = 'ABCDEF'
    for x in h.upper(): 
        if x in a:
            x = 10 + a.index(x)
        ans = ans + 16 ** power * int(x)
        power -= 1

    return ans

#def add(b, bb):
#     b = btod(b)
#     bb = btod(bb)
#     ans = b + bb
#     ans = dtob(ans)
#     return ans

print('Would you like to convert:')
print('1) Binary number to a decimal number')
print('2) Decimal number to a binary number')
print('3) Add two binary numbers')
print('4) Hexadecimal to binary number')
print('5) Binary to hexadecimal number')
print('6) Decimal to hexadecimal')
print('7) Hexadecimal to decimal')
a = input(': ')
if a == '1':
    binary = input('Enter a binary number: ')
    print(f'{binary} is {btod(binary)}!')
elif a == '2':
    decimal = input('Enter a decimal number: ')
    print(f'{decimal} is {dtob(decimal)}')
elif a == '3':
    num = input('Enter a binary number: ')
    num1 = input('Enter a second number: ')
    print(add(num, num1))
elif a == '4':
    hexadecimal = input('Enter a hexadecimal: ')
    print(f'{hexadecimal} is {htob(hexadecimal)}')
elif a == '5':
    binaryn = input('Enter a binary number: ')
    print(f'{binaryn} is {btoh(binaryn)}')
elif a == '6':
    dec = input('Enter a decimal number: ')
    print(f'{dec} becomes {dtoh(dec)}')
else:
    hexa = input('Enter a hexadecimal: ')
    print(f'{hexa} becomes {htod(hexa)} in decimal!')
    
        
    