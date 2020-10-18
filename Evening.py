def eve_amount(choosen_integer):
    if choosen_integer==3:
        print("Ho! Great ,Please Select your rides.")
        print()

        eve_programs=['1.Roller coaster','2.Gaint Wheel','3.Planitary Model'] 
        print()
        
        for i in eve_programs:
            print(i)
        print("Please enter the numericals.....")

        choosen_integer_eve=int(input())
        # if he choose 1
        if choosen_integer_eve==1:
            print("You can Pay 70/- to enjoy the show.")
            
            amount_toPay=int(input())
            if amount_toPay==70:
                print("Thank You, Enjoy the ride." )
            else:
                print("check the amount once again.....")
                while True:
                    print("check the amount once again.....")
                    if int(input())==70:
                        print("Thank You, Enjoy the ride." )
                    break
    
            # if he choose 2   
        if choosen_integer_eve==2:
            print("You can Pay 50/- to enjoy the ride.")
            
            amount_toPay=int(input())
            if amount_toPay==50:
                print("Thank You, Enjoy the ride." )
            else:
                print("check the amount once again.....")
                while True:
                    print("check the amount once again.....")
                    if int(input())==50:
                        print("Thank You, Enjoy the ride." )
                    break
             
             
             # if he choose 3

        if choosen_integer_eve==3:
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
        if choosen_integer_eve>3:
           print()
           print("oops you have entered a unvalid number.... ")
           print("Try again")
           eve_amount(choosen_integer)
           
    return