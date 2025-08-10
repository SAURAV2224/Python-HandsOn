def user_input():
    #variables
    choice = 'Some String'
    #acceptable range
    acpt_range = range(0,9)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input("Enter a number: ")

        if choice.isdigit()==False:
            print("Entered number is not digit ,re-enter......")

        if choice.isdigit():
            if int(choice) in acpt_range:
                within_range = True
            else:
                print("Entered number is outside acceptable range ,re-enter........")
            
    return int(choice)

result = user_input()
print(result)
