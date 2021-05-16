import random
import numpy as np

#random.seed(1)

def create_board():
    return np.zeros((3,3),dtype=int)

def place(board,player,position):
    board[position]=player

def possibilities(board):
    indi=np.where(board==0)
    return (list(zip(indi[0],indi[1])))

def random_place(board,player):
    availablepos=possibilities(board)
    if len(availablepos)!=0:
        place(board,player,random.choice(availablepos))  

def row_win(board,player):
    flag=0
    for i in range(3):
        flag=0
        for j in range(3):
            if board[i][j]==player:
                flag+=1
        if flag==3:
            return True
    return False

def col_win(board,player):
    for i in range(3):
        flag=0
        for j in range(3):
            if board[j][i]==player:
                flag+=1
        if flag==3:
            return True
    return False


def diag_win(board,player):
    flag1,flag2=0,0
    for i in range(3):
        if board[i][i]==player:
            flag1+=1
        if board[i][3-i-1]==player:
            flag2+=1
    if flag1==3 or flag2==3:
        return True
    return False

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # add your code here!
        if(row_win(board,player) or col_win(board,player) or diag_win(board,player)):
            winner = player
        pass
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def play_game():
    board=create_board()
    player=1
    while(np.any(board==0)):
        random_place(board,player)
        eval=evaluate(board)
        if eval!=0:
            return eval
        else:
            if player==1:
                player=2
            else:
                player=1

results=[]
count=0
for i in range(1000):
    temp=play_game()
    results.append(temp)
    if temp==1:
        count+=1
print("Winners:",results)
print("Number of times player1 won:",count)