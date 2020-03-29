#aliciacisneros A01281991
# 0 encrypt
# 1 decrypt
binary = "01"
octal = "0123456789."
english = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

englishPerm = "HCAGXLMYOBNZSWFVIPTUREJQDK"

def encryptAlphabet(alphabet,key, x):
    pos = alphabet.find(x)
    print(pos)
    return key[pos]

def decryptAlphabet(alphabet, key, x):
    pos = key.find(x)
    return alphabet[pos]

def substitution(action, key, alphabet, ciphertext):
  ciphertextAux = ""
  for x in ciphertext:
    str(x)
    if (alphabet.find(x) != -1 and action == 0):
        ciphertextAux += encryptAlphabet(alphabet,key,x)
    elif (alphabet.find(x) != -1 and action):
        ciphertextAux += decryptAlphabet(alphabet,key,x)
    else:
        ciphertextAux += x
  print(ciphertextAux)

substitution(0, englishPerm, english, "BART")
substitution(1, englishPerm, english, "CHPU")