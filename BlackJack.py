# BLACKJACK: Given three integers between 1 and 11,if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
#  Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

# def blackjack(a,b,c):
#     lst=[a,b,c]
#     sumt=0
#     for i in range(len(lst)):
#         if lst[i]==11:
#             sumt+=1
#         else:
#             sumt+=lst[i]
#     if sumt>21:
#         return "'BUST'"
#     else:
#         return sumt

def blackjack(a,b,c):
    sumt=0
    if a==11 or b==11 or c==11:
        sumt=a+b+c-10
    else:
        sumt=a+b+c
    
    if sumt>21:
        return "'BUST'"
    else:
        return sumt

    
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))