import sys

key = int(sys.argv[1])
message = ""

char_count = 0
block_count = 0

for line in sys.stdin:
  for letter in line:
    if letter.isalpha():
      
      if char_count == 5:
        block_count += 1
        message += " "
        char_count = 0
        
      if block_count == 10:
        message += "\n"
        block_count = 0
      
      char_count += 1

      letter = letter.upper()
      new_letter = chr(ord(letter) + key)
      if ord(new_letter) > 90:
        new_letter = chr(ord(letter) + key - 26)
      message += new_letter

  break

print(message)