import os
hostname = input("Email: ")
response = os.system("ping -n 1 " + hostname)
if response == 0:
    pingstatus = "Network Active"
else:
    pingstatus = "Network Error"

input()    