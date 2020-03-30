#aliciacisneros a01281991
english = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 0 = encrypt
# 1 = decrypt

def createMatrix(rows,cols,ciphertext):
  matrix = [["" for x in range(cols)] for y in range(rows)]
  for i in range(rows):
    for j in range(cols):
      if(((i * cols) + j ) <= len(ciphertext) - 1):
        matrix[i][j] = ciphertext[(i * cols) + j ]

  return matrix

def readMatrix(rows, cols, matrix):
  ciphertextAux = ""
  for i in range(cols):
    for j in range(rows):
      ciphertextAux += matrix[j][i]
  return ciphertextAux
     
def decryptAlphabet(ciphertext, key):
  rows = len(key) # 7
  lenCiphertext = len(ciphertext) # 20
  if(lenCiphertext % rows  != 0):
    cols = int((lenCiphertext / rows) + 1 )
  else:
    cols = int(lenCiphertext / rows)
  matrix = createMatrix(rows,cols,ciphertext)
  return readMatrix(rows,cols,matrix)


def encryptAlphabet(ciphertext, key):
  col = len(key) # 7
  lenCiphertext = len(ciphertext) # 20
  if(lenCiphertext % col  != 0):
    rows = int((lenCiphertext / col) + 1 )
  else:
    rows = int(lenCiphertext / col)
  matrix = createMatrix(rows,col,ciphertext)
  return readMatrix(rows,col,matrix)

def transposition(ciphertext, key, action):
  ciphertextAux = ""
  ciphertext = ciphertext.replace(" ", "")
  if(action == 1):
    print(decryptAlphabet(ciphertext, key))
  else:
    print(encryptAlphabet(ciphertext,key))

transposition("MAY THE FORCE BE WITH YOU", "SIDIOUS", 0)
transposition("MOIARTYCHTEYHBOEEUFW", "SIDIOUS", 1)

