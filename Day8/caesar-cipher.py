alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
  output_text = ''
  for letter in text:
    if direction == 'encode':
      if (alphabet.index(letter) + shift) > 25:
        output_text += alphabet[(alphabet.index(letter) + shift)]
      else:  
        output_text += alphabet[(alphabet.index(letter) + shift)]
    if direction == 'decode':
      if (alphabet.index(letter) + shift) > 25:
        output_text += alphabet[(alphabet.index(letter) - shift)]
      else:  
        output_text += alphabet[(alphabet.index(letter) - shift)]

  print(f"The {direction}d text is {output_text}")

should_continue = True

while should_continue:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  while not (direction == 'encode' or direction == 'decode'):
    print('Invalid input\n')
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n")) 
  if shift > 25:
    shift = shift % 26
  caesar(direction, text, shift)

  decision = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
  if decision == 'no':
    should_continue = False