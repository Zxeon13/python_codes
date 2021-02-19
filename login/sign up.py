while True:
    username = input('Enter new Username: ')
    usernametxt='files/'+username+".txt"
    try:
        if open( usernametxt , 'r'):
            print("This username is taken, plez try again.")
    except:
        break
 
userdict={'username':username,'email':'','password':'','other_data':''}
userdict['email']=input('Please enter a valid email address: ')

password=None
while True:
    password= input('Enter a new password: ')
    userdict['password']=input('Conferm the new password: ')
    if password != userdict['password']:
        print('Passwords dont match,please renter them.')
    elif password == userdict['password']:
        break


userdict['other_data']=input('Enter any other data you like: ')
userfile = open(usernametxt,'a')
for k,v in userdict.items():
    userfile.writelines(k+"::"+v+"::\n")
print("Done!")