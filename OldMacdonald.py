# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(str):
    newStr =''
    for i in range(0,len(str)):
        if(i==0 or i==3):
            newStr+= str[i].upper()
        else:
            newStr+= str[i]

    return newStr

print(old_macdonald('macdonald'))