# ANIMAL CRACKERS: Write a function takes a two-word string
#  and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(str):
    lst = str.split()
    if lst[0][0] == lst[1][0]:
        return True
    else:
        return False
    
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))