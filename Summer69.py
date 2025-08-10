# SUMMER OF '69: Return the sum of the numbers in the array, 
# except ignore sections of numbers starting with a 6 and extending to the next 9
#  (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

# def summer_69(lst):
#     sumt=0
#     id1=-1
#     id2=0
#     for i in range(len(lst)):
#         if lst[i]==6:
#             id1=i
#         elif i>id1 and lst[i]==9:
#             id2=i
#         elif id1 < 0:
#             sumt+=lst[i]
#         elif id1>0 and id2==0:
#             pass
#         else:
#             sumt+=lst[i]
#     return sumt



def summer_69(nums):
    entry=True
    sum=0
    for num in nums:
        if num==6:
            entry=False
            continue
        if num==9 and entry==False:
            entry=True
            continue
        if entry == True:
            sum+=num
    return sum



print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
