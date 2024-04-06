with open('sampleInput.txt', encoding='utf-8') as fp:
    filedata = fp.read()


def dtob(dnum):
    bnums = []
    ans = int(dnum)
    while ans != 0:
        remainder = ans % 2
        ans = ans // 2
        bnums.append(str(remainder))
    bnums.reverse()
        
    return ''.join(bnums)


def utf(s):
    result = ''
    for c in s:
        d = ord(c)
        binary = dtob(d)
        l = len(binary)

        if l <= 7:
            if l != 7:
                binary = '0' * (7 - l) + binary
            result = result + '0' + binary
            
        elif l <= 11:
            if l != 11:
                binary = '0' * (11 - l) + binary
            r = '110' + binary[:5] + '10' + binary[5:]
            result = result + r
            
        elif l <= 16:
            if l != 16:
                binary = '0' * (16 - l) + binary
            r = '1110' + binary[:4] + '10' + binary[4:10] + '10' + binary[10:]
            result = result + r

            
        elif l <= 21:
            if l != 21:
                binary = '0' * (21 - l) + binary
            r = '11110' + binary[:3] + '10' + binary[3:9] + '10' + binary[9:15] + '10' + binary[15:]
            result = result + r


    return result

def btod(bnum):
    dnum = 0
    power = len(bnum) - 1
    for n in bnum:
        dnum += int(n) * 2 ** power
        power -= 1
    return dnum
      
def decode(b):
    p = 0
    strip = ''
    res = ''
    
    while p < len(b):
        if b[p] == '0':
            charb = b[p:p+8]
            p += 8
            strip = charb
        elif b[p:p+3] == '110':
            charb = b[p:p+16]
            p += 16
            strip = charb[3:8] + charb[10:]
        elif b[p:p+4] == '1110':
            charb = b[p:p+24]
            p += 24
            strip = charb[4:8] + charb[10:16] + charb[18:]
        elif b[p:p+5] == '11110':
            charb = b[p:p+32]
            p += 32
            strip = charb[5:8] + charb[10:16] + charb[18:24] + charb[26:]
        res = res + chr(btod(strip))
    return res


sen = input('Type a sentence: ')
print(f'This sentence encoded is: {utf(sen)}')
coded = input('Enter a coded message: ')
print(f'This message decoded is: {decode(coded)}')
