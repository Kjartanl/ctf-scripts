
import sys

def encrypt(input):
    letters_and_positions = get_letters_and_positions(input)
    new_letters = [get_next_char(char, pos) for (char, pos) in letters_and_positions]
    letters = [get_next_char(char, pos) for (char, pos) in letters_and_positions]
    return letters

def decrypt(input):
    letters_and_positions = get_letters_and_positions(input)
    letters = [get_next_char(char, pos * -1) for (char, pos) in letters_and_positions]
    return letters
    

def get_next_char(char, pos):
    #print("char: %s, pos: %s" % (char, pos))
    numeric = ord(char)
    next_numeric = numeric + pos
    return chr(next_numeric)

def get_letters_and_positions(input):
    return [(char, pos) for (pos, char) in enumerate(input)]
    
nr_of_args = len(sys.argv) 

if(nr_of_args < 2 or nr_of_args > 3):
    print("Wrong nr. of args. Use: [-encrypt] 'targetword'")
elif (nr_of_args == 2):
   output = decrypt(sys.argv[1])
   print("Resulting cleartext: %s" % ''.join(output))
elif (sys.argv[1] == '-encrypt'):
   output = encrypt(sys.argv[2])
   print("Resulting ciphertext: %s" % ''.join(output))
