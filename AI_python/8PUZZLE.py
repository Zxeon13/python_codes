import click , os
state_board=['1','2','3','4','5','6','7',' ','8']
goal_board=['1','2','3','4','5','6','7','8',' ']
closed_list=[]
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
        print("invalid move!")
        return state
    try:
            state[inx_0]=state[inx_n]
            state[inx_n]=" "
            return state
        
    except:
        print("invalid move!")
        return state
       
  
g_n=0  
tmp_board = state_board
while True:
    h_n=H(tmp_board)
    f_n = h_n+g_n
    show_bord(tmp_board)
    print(f'F(n)={g_n}+{h_n}={f_n}' )
    mov = click.getchar().upper()
    inx_0=tmp_board.index(' ')
    inx_n=inx_0
    if mov=="W":
        inx_n-=3
    elif mov=="S":
        inx_n+=3
    elif mov=="A":    
        if inx_0%3 != 0:
            inx_n=inx_0-1 
    elif mov=="D":    
        if inx_0%3 != 2:
            inx_n=inx_0+1
    else:
        print("invad input!")
        continue

    tmp_board= mover(tmp_board,inx_n,inx_0)
    if tmp_board in closed_list:
        pass
    else:
        g_n+=1
        closed_list.append(tmp_board)
    if H(tmp_board) == 0  :
        show_bord(tmp_board)
        print(f"CONGRATLATION!!\nYOU DID IT IN {g_n} moves!!!")
        input()
        break


