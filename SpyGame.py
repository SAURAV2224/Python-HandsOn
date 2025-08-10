# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(lst):
    id=0
    for i in range(len(lst)):
        if id==0 and lst[i]==0:
            id+=1
        elif id==1 and lst[i]==0:
            id+=1
        elif id==2 and lst[i]==7:
            id+=1
        else:
            pass


    
    if id==3:
        return True
    else:
        return False
    
 
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]) )
print(spy_game([1,7,2,0,4,5,0]) )
