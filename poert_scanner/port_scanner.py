import socket
from termcolor import colored
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(2)
host= input("[*]Enter target ip: ")
def scanner(port):
    if sock.connect_ex((host,port)):
        print(colored("[-]port %d is closed" %(port),'red'))
    else:
        print(colored("[+]port %d is open" %(port) ,'green',attrs=['bold']))   
for port in range(1001):
    scanner(port)

input