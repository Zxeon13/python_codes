import time,re,pyautogui
def space_deleter(x):
    return str(x != "  ")


def clickTab(y):
    x= int(y)
    for i in range(0,x):
        pyautogui.press("enter")

f = open("test2.txt",'r',encoding='utf-8')
for line in f:
    if "[" in line:
        for i in line:
            y=""
            z=0
            for i in line:
                y = y +i
                if i ==" " and line[z+1] ==" " and line[z+2] == " ":
                    y = y + "\n"    
                z=z+1
                print(re.sub(r'\n\s*\n','\n',y,re.MULTILINE))
 
