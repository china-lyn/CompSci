# Caeser cipher

message = input('Type in a phrase: ')
key = int(input('What key number do you want for this code?: '))
code = input('Type "e" to encode or "d" to decode your message: ')
if code == 'd':
    key = -key
    
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

output = ''

for x in message.upper():
    index = alphabet.find(x)
    if index == -1:  
        output = output + x
        continue
    elif index < 25 - key:
        offset = key
    else:
        offset = key - 26

    output = output + alphabet[index + offset]

print(output)
