import re 
import string

Alphabet=string.ascii_uppercase
message=input("Enter the message : ").upper()
x = input('Enter(E) to Encode the message or (D) to Decode it : ').upper()
key = int(input('Enter the key lenth: '))
if x =='D' :key=-key
newMessage=""
for letter in range(len(message)):
    if re.search('[A-Z]',message[letter]):
        index=Alphabet.find(message[letter])
        newIndex=(index+key)%26
        newMessage += Alphabet[newIndex]
    else:
        newMessage += message[letter]

print(newMessage)    
