import re 
import string

Alphabet=string.ascii_uppercase
message=input("Enter the message : ").upper()
x = input('Enter(E) to Encode the message or (D) to Decode it : ').upper()
key = input('Enter the key : ').upper()
newMessage=""
for letter in range(len(message)):
    if re.search('[A-Z]',message[letter]):
        index=Alphabet.find(message[letter])
        key_index=Alphabet.find(key[letter%len(key)])
        if x == 'D':
            newIndex=(index-key_index)%26
        else:
            newIndex=(index+key_index)%26
        newMessage += Alphabet[newIndex]
    else:
        newMessage += message[letter]

print(newMessage)    
