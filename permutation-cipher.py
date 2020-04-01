#aliciacisneros a01281991
# english = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # 0 = encrypt
# # 1 = decrypt

def decrypt(key, ciphertext):
    return encrypt(inverse_key(key), ciphertext)

def encrypt(key, plaintext):
    plaintext = "".join(plaintext.split(" ")).upper()
    ciphertext = ""
    for extraLetter in range(0, len(plaintext) % len(key) * -1 % len(key)):
        plaintext += "Z"
    for i in range(0, len(plaintext), len(key)):
        for element in [a - 1 for a in key]:
            ciphertext += plaintext[i + element]
        ciphertext += " "
    return ciphertext

def inverse_key(key):
    inverse = []
    for position in range(min(key),max(key )+ 1,1):
        inverse.append(key.index(position)+1)
    return inverse


print(encrypt([2,4,1,5,3], "COWABUNGA"))
print(decrypt([2,4,1,5,3], encrypt([2,4,1,5,3], "COWABUNGA")))