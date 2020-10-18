def aft_amount(choosen_integer):
    if choosen_integer==2:
        print("Ho! Great ,Please Select your rides.")
        print()

        aft_programs=['1.Water rides','2.Under the Water','3.Wave Pool'] 
        print()
        
        for i in aft_programs:
            print(i)
        print("Please enter the numericals.....")

        choosen_integer_aft=int(input())
        # if he choose 1
        if choosen_integer_aft==1:
            print("You can Pay 80/- to enjoy the show.")
            
            amount_toPay=int(input())
            if amount_toPay==80:
                print("Thank You, Enjoy the show." )
            else:
                print("check the amount once again.....")
                while True:
                    print("check the amount once again.....")
                    if int(input())==80:
                        print("Thank You, Enjoy the show." )
                    break
    
            # if he choose 2   
        if choosen_integer_aft==2:
            print("You can Pay 100/- to enjoy the show.")
            
            amount_toPay=int(input())
            if amount_toPay==100:
                print("Thank You, Enjoy the show." )
            else:
                print("check the amount once again.....")
                while True:
                    print("check the amount once again.....")
                    if int(input())==100:
                        print("Thank You, Enjoy the show." )
                    break
             
             
             # if he choose 3

        if choosen_integer_aft==3:
            print("You can Pay 120/- to enjoy the show.")
            
            amount_toPay=int(input())
            if amount_toPay==120:
                print("Thank You, Enjoy the show." )
            else:
                print("check the amount once again.....")
                while True:
                    print("check the amount once again.....")
                    if int(input())==120:
                        print("Thank You, Enjoy the show." )
                    break
        if choosen_integer_aft>3:
            print()
            print("oops you have entered a unvalid number.... ")
            print("Try again")
            aft_amount(choosen_integer)

    return