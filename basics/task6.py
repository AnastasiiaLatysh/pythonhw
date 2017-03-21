def caesar_cipher(plainText, shift):
  cipherText = ""
  for ch in plainText:
    if ch.isalpha():
      stayInAlphabet = ord(ch) + shift
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
  return cipherText




str = 'Our string'
print("Before caesar_cipher function: ", str)
intNumber = 1
print("After caesar_sipher function: ", caesar_cipher(str, intNumber))

