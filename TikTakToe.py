import os
import platform

def clear_console():
    if platform.system=='Windows':
        os.system('cls')
    else:
        os.system('cls')



def display_board(board):
    print('      |        |       ')
    print(' '+board[7]+'    |   '+board[8]+'    |   '+board[9]+'  ')
    print('      |        |       ')
    print('-----------------------')
    print('      |        |       ')
    print(' '+board[4]+'    |   '+board[5]+'    |   '+board[6]+'  ')
    print('      |        |       ')
    print('-----------------------')
    print('      |        |       ')
    print(' '+board[1]+'    |   '+board[2]+'    |   '+board[3]+'  ')
    print('      |        |       ')
    return

def assign_marker():
    valid_entry=False
    ava_markers=['X','O','x','o']
    marker1 = 'One'
    marker2 = 'Two'
    while valid_entry==False:
        marker1=input("Choose the marker for Player1 'O' or 'X'")
        if marker1 in ava_markers:
            valid_entry=True
        else:
            print("Invalid entry.,re-enter!!!!!!!!!")

    marker1= marker1.upper()
    if marker1=='X':
        marker2='O'
    else:
        marker2='X'
    
    return [marker1,marker2]

def possible_victory(board,player):
    if board[1]!=' ':
        if board[1]==board[2] and board[2]==board[3]:
            return True
    if board[4]!=' ': 
        if board[4]==board[5] and board[5]==board[6]:
            return True
    if board[7]!=' ':
        if board[7]==board[8] and board[8]==board[9]:
            return True
    if board[1]!=' ':
        if board[1]==board[4] and board[4]==board[7]:
            return True
    if board[2]!=' ':
        if board[2]==board[5] and board[5]==board[8]:
            return True
    if board[3]!=' ':
        if board[3]==board[6] and board[6]==board[9]:
            return True
    if board[1]!=' ':
        if board[1]==board[5] and board[5]==board[9]:
            return True
    if board[3]!=' ':
        if board[3]==board[5] and board[5]==board[7]:
            return True
    
    return False
        
def each_entry(board,player,seen,player_no):

    position=0
    validEntry=False
    while validEntry==False:
        position=input(player_no +"'s turn - Enter the position : ")
        #check entry not string
        if position.isdigit()==False:
            print("Invalid Entry, please re-enter a number!!!")
            continue
        position=int(position)

        #check entry in range
        if position not in range(1,10):
            print("Invalid Entry, please re-enter!!!")
            continue
        
        #check entry not previously filled
        if position in seen:
            print("Position already filled.Enter another unfilled position !!!!")
        else:
            seen[position]=1
            validEntry=True

    board[position]=player
    display_board(board)
    return board,seen


def lets_play():
     #assign board value to blank
    board=[' ']*10

    #print board after each update
    display_board(board)

    #assign markers for both players
    mark = assign_marker()
    P1 = mark[0]
    P2 = mark[1]

    seen={}
    count=0

    #take entery -first player followed by second player
    while count < 9:
        if count%2==0:
          each_entry(board,P1,seen,"Player1")
          count+=1
          if possible_victory(board,P1):
              print("Player1 is victorious")
              break
        else:
            each_entry(board,P2,seen,"Player2")
            count+=1  
            if possible_victory(board,P2):
              print("Player2 is victorious")
              break 

    return 

clear_console()
lets_play()

