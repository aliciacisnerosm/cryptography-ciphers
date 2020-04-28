#aliciacisneros a01281991
english = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
import math  

def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1
   
# (position * key )% 26
def encryptAlphabet(alphabet,ciphertext, key):
  posKey = (int((alphabet.find(ciphertext))) * key) % len(alphabet)
  return alphabet[posKey]

def decryptAlphabet(alphabet, ciphertext, key):
  posKey = int(alphabet.find(ciphertext)) * int(modInverse(key,len(alphabet))) % len(alphabet)
  return alphabet[posKey]


def multiplicative(action, key, alphabet, ciphertext):
  ciphertextAux = ""
  ciphertext = ciphertext.replace(" ", "")
  for x in ciphertext:
    str(x)
    if (alphabet.find(x) != -1 and action == 0):
        ciphertextAux += encryptAlphabet(alphabet,x, key)
    elif(alphabet.find(x) and action == 1):
      ciphertextAux += decryptAlphabet(alphabet, x, key)
    else: 
        ciphertextAux += x  
  print (ciphertextAux)

multiplicative(1, 7, english, "GAMDXCJUPOCHCYEDXMUK")
