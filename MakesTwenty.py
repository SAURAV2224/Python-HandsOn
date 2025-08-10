# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 
# or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def makes_twenty(a,b):
    if a == 20 or b == 20:
        return True
    elif a+b == 20:
        return True
    else:
        return False
print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))
