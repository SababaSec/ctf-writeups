chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
target = 0x1371fcaacf98

def getValue(char):
    value = ord(char)
    if value < 0x3a:
        value += 0x4
    elif value < 0x5b:
        value -= 0x41
    else:
        value -= 0x47
    return value

def getFlag():
    flag = ''
    total = 0
    for i in range(8):
        total *= 0x3e
        prev = ''
        for c in chars:
            if (total + getValue(c)) * 0x3e ** (7 - i) > target:
                break
            prev = c
        flag += prev
        total += getValue(prev)
    
    print('nactf{' + flag + '}')
getFlag()
