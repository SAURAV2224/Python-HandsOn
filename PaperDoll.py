# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(str):
    newStr=''
    for i in range(len(str)):
        newStr+=str[i]*3

    return newStr

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))