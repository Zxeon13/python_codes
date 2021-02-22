import re 
import string

Alphabet=string.ascii_uppercase
message=input("Enter the message that will be ckracked : ").upper()
for key in range(26):
    newMessage=""
    for letter in range(len(message)):
        if re.search('[A-Z]',message[letter]):
            index=Alphabet.find(message[letter])
            newIndex=(index-key)%26
            newMessage += Alphabet[newIndex]
        else:
            newMessage += message[letter]

    print("with key :",key,"the message :",newMessage)    
