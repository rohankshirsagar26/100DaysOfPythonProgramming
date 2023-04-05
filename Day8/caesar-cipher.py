alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

while not (direction == 'encode' or direction == 'decode'):
  print('Invalid input\n')
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  cipher_text=''
  for letter in text:
    if (alphabet.index(letter) + shift) > 25:
      cipher_text += alphabet[(alphabet.index(letter) + shift) - 26]
    else:  
      cipher_text += alphabet[(alphabet.index(letter) + shift)]
  print(f"The encoded text is {cipher_text}")


def decrypt(text, shift):
  cipher_text = ''
  for letter in text:
    if (alphabet.index(letter) + shift) > 25:
      cipher_text += alphabet[(alphabet.index(letter) - shift) - 26]
    else:  
      cipher_text += alphabet[(alphabet.index(letter) - shift)]
  print(f"The decoded text is {cipher_text}")

if direction == 'encode':
  encrypt(text = text, shift = shift)
elif direction == 'decode':
  decrypt(text = text, shift = shift)