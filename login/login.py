while True:
    username = input('Enter your Username: ')
    usernametxt='files/'+username+".txt"
    try:
        if open( usernametxt , 'r'):
            break
    except:
        print('Username unvalede,please try again or sign up.')
f= open(usernametxt,'r')

userdict=dict()
for i in f:
    items=i.split("::")
    userdict[items[0]]=items[1]

while True:
    password=input("Enter your password: ")
    if password == userdict['password']:
        print("Welcome!",userdict['username'])
        break
    else:
        print("Password incorect,try again.")
input()