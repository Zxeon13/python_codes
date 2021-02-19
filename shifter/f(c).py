file = input('Enter the increpted code: ')
x = int(input('enter "26" to incrept the data or "-26" to decrept it: '))
key = int(input('Enter the key lenth: '))
if x <0:key=-key
newfile=''    
for letter in file   :
    if letter != ' ':
        letter_num= ord(letter)+key
        if letter_num < 97 and letter_num >90 or letter_num <65 : letter_num=letter_num+x
        newfile = newfile+chr(letter_num)  
    if letter == ' ':
        newfile = newfile +letter  

print('the output is:',newfile)