#alicia cisneros A01281991
binary = "01"
octal = "0123456789."
english = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 0 = encrypt
# 1 = decrypt

def encryptAlphabet(alphabet, key, x):
  num = int(alphabet.find(x))
  num = ((num + key) % len(alphabet))
  return alphabet[num]


def decryptAlphabet(alphabet, key, x):
  num = int(alphabet.find(x))
  num = ((num - key) % len(alphabet))
  return alphabet[num]

def shift(alphabet, ciphertext, key, action):
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

shift(english, "LSDO WI CRSXI WODKV KCC", 10,1)
shift(english, "LET MORTAL KOMBAT BEGIN", 13,0)
shift(english, "JKGJ UX GROBK EUAXK IUSOTM COZN SK", 6,1)
shift(binary, '101010', 3, 0)
shift(octal, "73585926.979120276718", 4,1)







