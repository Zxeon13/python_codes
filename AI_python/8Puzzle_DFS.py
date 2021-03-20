import os
from typing import Counter
state_board=['1','2','3','4','5','6','7',' ','8']

def H(board):
    goal=['1','2','3','4','5','6','7','8',' ']
    board=list(board)
    h_n=0
    for i in range(8):
        if board[i] != goal[i]:
            h_n+=1
    return h_n

def show_bord(x):
    os.system("cls")
    print("["+x[0]+"]["+x[1]+"]["+x[2]+"]\n["+x[3]+"]["+x[4]+"]["+x[5]+"]\n["+x[6]+"]["+x[7]+"]["+x[8]+"]\n")

def mover(state,inx_n,inx_0):
    state=list(state)
    if inx_n<0:
        return state
    try:
            state[inx_0]=state[inx_n]
            state[inx_n]=" "
            return state
    except:
        return state
       

def DFS(state_board):
    g_n=0  
    mov=0
    closed_list=[]
    tmp_board = state_board
    closed_list.append(tmp_board)
    show_bord(tmp_board)

    while True:
        inx_0=tmp_board.index(' ')
        inx_n=inx_0
        if mov==0:
            inx_n-=3
        elif mov==2:
            inx_n+=3
        elif mov==3:    
            if inx_0%3 != 0:
                inx_n=inx_0-1 
        elif mov==1:    
            if inx_0%3 != 2:
                inx_n=inx_0+1
        elif mov==4:
            mov=0 
            tmp_board=closed_list[g_n-2]
            g_n-=1
            continue

        tmp_board= mover(tmp_board,inx_n,inx_0)

        if tmp_board in closed_list:
            mov=mov+1
            continue
      
        else:
            show_bord(tmp_board) 
            print("added 2 the lest")
            g_n+=1
            closed_list.append(tmp_board)
        

        if H(tmp_board) == 0  :
            num=len(closed_list)
            print(f"CONGRATLATION!!\nYOU NEEDED {num} moves!!!")
            break

DFS(state_board)
input()
