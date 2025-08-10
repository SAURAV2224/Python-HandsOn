# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(str):
    newStr=''
    lst=str.split()
    lst= lst[::-1]
    for i in range(0,len(lst)):
        if i < len(lst):
            newStr+=lst[i]+' '
        else:
            newStr+=lst[i]
    return newStr

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

