import os
import platform

#constants
win_combo = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

#clear console output
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

#check if the player has won -VVIP
def check_win(board,player):
    for combo in win_combo:
        check=[]
        for pos in combo:
           check.append(board[pos]==player) 
        if all(check):
            return True
    return False

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
      
def each_entry(board,player,player_no):

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
        if board[position]!=' ':
            print("Position already filled.Enter another unfilled position !!!!")
        else:
           validEntry=True

    board[position]=player
    display_board(board)
    return board

def play_again():
    lst=['Y','N']
    validEntry = False

    while validEntry == False:
        play = input("Enter Y/N if you want to play again : ")
        if play in lst:
            if play=='Y':
                return True
            else:
                return False
    return

def lets_play():
     #assign board value to blank
    board=[' ']*10

    #print board after each update
    display_board(board)

    #assign markers for both players
    mark = assign_marker()
    P1 = mark[0]
    P2 = mark[1]

    count=0

    #take entery -first player followed by second player
    while count < 9:
        if count%2==0:
          each_entry(board,P1,"Player1")
          count+=1
          if check_win(board,P1):
              print("Player1 is victorious")
              break
        else:
            each_entry(board,P2,"Player2")
            count+=1  
            if check_win(board,P2):
              print("Player2 is victorious")
              break 

        if count==8:
            print("Match Drawn!!!!!!!!!!!!!!")

    if play_again():
        clear_console()
        lets_play()
    
    return 

#function call for game to start
clear_console()
lets_play()

