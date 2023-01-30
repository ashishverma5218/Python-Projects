intro = input("Welcome ! Can you want to play KBC ? (y/n) ")
if intro.lower() == 'y':
    print('Here are 5 Questions.You have to answer.If you give right answer.You win money.\n \n---First Question---\n')
    first = int(input(" How many years are there in a decade?  "))
    if first == 10:
        print("Right answer !  \n \n ----Second Question----\n")
        second = int(input("How many months have 30 day. "))
        if second == 4:
            print("Right answer !   \n \n----Third Question----\n")
            Third = int(input(" 106 × 106 – 94 × 94 = ? "))
            if Third == 2400:
                print("Right answer !   \n \n----Fourth Question----\n")
                fourth = int(input("Fill in the blanks; 4, 6, 12, 14, 28, 30, (?) "))
                if fourth == 60:
                    print("Right answer !   \n \n----Fifth Question----\n")
                    Fifth = int(input(" Speed of a car is 60 km/hr. Distance covered in 1 ¼ hours is ? "))
                    if Fifth == 75:
                        print("Right answer !\n \n---You give all right answer so you won 500 ka ek Purana note---\n")
                    else:
                        print("You Loose ! Better luck next time. ")
        else:
            print("You Loose ! Better luck next time. ")
    else:
        print("You Loose ! Better luck next time. ")
else:
    print("Thanks for visiting ! ")
