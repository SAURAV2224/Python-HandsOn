#output screen

def game_display(game_list):
    print(game_list)
    return 

#take user entry to change position
def position():
    str = ['0','1','2']
    valid_entry = False
    
    while valid_entry == False:
        choice = input("Enter the Index position you want to update(0-2): ")
        if choice in str:
            return int(choice)
        else:
            print("Invalid Entry!!!!!!!!!")
        
    return

def take_value(position):
    
    entry_valid=False
    while entry_valid==False:
        value = input("Enter the String you want to replace '"+ str(position) +"' Index with (word length = 5) : ")
        if len(value) < 6:
            return value
        else:
            print("Word too long ,please re-enter!!!!!!!")
    return 

def update_value(gamelist,position,value):
    gamelist[position]=value
    print("The updated list : ")
    print(gamelist)
    return gamelist

def ask_toPlay():
    entry_valid=False
    while entry_valid==False:
        value = input("Enter Y/N if you want to continue or not: ")
        if value=='Y':
            return True
        elif value=='N':
            return False
        else:
            print("In-valid entry,please re-enter.....")
        
    return
    

def game_exe():
    gamelist=[0,1,2]
    game_display(gamelist)
    pos =position()
    value=take_value(pos)
    update_value(gamelist,pos,value)
    while ask_toPlay():
        game_display(gamelist)
        pos =position()
        value=take_value(pos)
        update_value(gamelist,pos,value)
    return

game_exe()
