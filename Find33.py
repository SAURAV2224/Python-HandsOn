# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(lst):
    ind = lst.index(3)
    for i in range(len(lst)-1):
        if lst[i]==3 and lst[i+1]==3:
            return True
        else:
            i+=1
    return False

print(has_33([1, 3, 3]) )
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
 