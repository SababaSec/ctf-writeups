arr = [52, 54, 60, 40, 72, 64, 42, 35, 93, 26, 38, 110, 3, 47, 56, 26, 64, 1, 49, 33, 71, 38, 7, 25, 20, 92, 1, 9]
key = 'Opportunity'
flag = ''

for i in range(28):
    flag += chr(arr[i] ^ ord(key[i % len(key)]))

print(flag)
