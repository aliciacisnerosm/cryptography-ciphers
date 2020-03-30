#aliciacisneros a01281991
english = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encryptAlphabet(alphabet,ciphertext, key):
 posKey = (int(alphabet.find(ciphertext)) * key) % len(alphabet)
 return alphabet[posKey]


def multiplicative(action, key, alphabet, ciphertext):
  ciphertextAux = ""
  ciphertext = ciphertext.replace(" ", "")
  for x in ciphertext:
    str(x)
    if (alphabet.find(x) != -1 and action == 0):
        ciphertextAux += encryptAlphabet(alphabet,x, key)
    else:
        ciphertextAux += x
  print(ciphertextAux)

multiplicative(0, 7, english, "MAY THE FORCE BE WITH YOU")