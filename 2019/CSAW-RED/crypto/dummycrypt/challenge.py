#Here's the encryptor code:

def encrypt(string, key):
    out = ""
    for s in range(len(string)):
        c = ord(string[s])
        c += ord(key[s%len(key)]) - ord('A')
        c = chr(c - ord('A'))
        out += c
    return out

#Here's the plaintext:
# Hellothere everybody how are you doing today_long-plaintexts-are fun
#Here's the ciphertext:
# 2c4f4b5168535a574f57064853485e5b3f5c4856124e525402406942076b60521156565358440057615644693c5e554d530a605d4064525e445d6d521f534f5706495251