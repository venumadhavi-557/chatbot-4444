def morg_amount(choosen_integer):
    if choosen_integer==1:
        print("Ho! Great ,Please Select your rides.")
        print()

        mrng_programs=['1.Dolphin show','2.ethic museum','3.The Snake Hunt'] 
        print()
        
        for i in mrng_programs:
            print(i)
        print("Please enter the numericals.....")

        choosen_integer_mrng=int(input())
        # if he choose 1
        if choosen_integer_mrng==1:
            print("You can Pay 70/- to enjoy the show.")
            
            amount_toPay=int(input())
            if amount_toPay==70:
                print("Thank You, Enjoy the show." )

            else:
                print("check the amount once again.....")
                while True:
                    print("check the amount once again.....")
                    if int(input())==70:
                        print("Thank You, Enjoy the show." )
                    break
    
            # if he choose 2   
        if choosen_integer_mrng==2:
            print("You can Pay 50/- to enjoy the show.")
            
            amount_toPay=int(input())
            if amount_toPay==50:
                print("Thank You, Enjoy the show." )
            else:
                print("check the amount once again.....")
                while True:
                    print("check the amount once again.....")
                    if int(input())==50:
                        print("Thank You, Enjoy the show." )
                    break
             
             
             # if he choose 3

        if choosen_integer_mrng==3:
            print("You can Pay 60/- to enjoy the show.")
            
            amount_toPay=int(input())
            if amount_toPay==60:
                print("Thank You, Enjoy the show." )
            else:
                print("check the amount once again.....")
                while True:
                    print("check the amount once again.....")
                    if int(input())==60:
                        print("Thank You, Enjoy the show." )
                    break
        if choosen_integer_mrng>3:
            print()
            print("oops you have entered a unvalid number.... ")
            print("Try again")
            morg_amount(choosen_integer)

    return