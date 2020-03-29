#aliciacisneros A01281991
# 0 encrypt
# 1 decrypt
binary = "01"
octal = "0123456789."
english = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encryptAlphabet(alphabet,key, x, keyPos):
    pos = alphabet.find(x) 
    keyLetter = alphabet.find(key[keyPos])
    pos = (pos + keyLetter) % len(alphabet)     
    return alphabet[pos]

def decryptAlphabet(alphabet, key, x, keyPos):
    pos = alphabet.find(x) 
    keyLetter = alphabet.find(key[keyPos]) 
    pos = (pos - keyLetter) % len(alphabet) 
    return alphabet[pos]


def vignere(action, key, alphabet, ciphertext):
  ciphertextAux = ""
  keyPos = 0
  for x in ciphertext:
    str(x)
    if (alphabet.find(x) != -1 and action == 0):
        ciphertextAux += encryptAlphabet(alphabet,key, x, keyPos)
    elif (alphabet.find(x) != -1 and action):
        ciphertextAux += decryptAlphabet(alphabet,key,x, keyPos)
    else:
        ciphertextAux += x
    keyPos = (keyPos + 1 ) % len(key)
  print(ciphertextAux)

vignere(0, "RED", english, "BART")
vignere(1, "RED", english, "SEUK")