def reverese_number():
    num = int(input("Enter a number : "))
    rev_num=0
    while num > 0:
        n=num%10
        num=int(num/10)
        rev_num=(rev_num*10)+n
    return rev_num
        
print(f'The reverse of the input number is : {reverese_number()}')
