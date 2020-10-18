""" 
This is program for a  chat bot ....
1. The bot will greet by welcoming to the amusement park and ask for his name.

2. The bot will give choices about the rides based on the timming on which they run.

3. The person choose the ride timing (morning ,afternoon,evening)

4. Once the choice it will display the rides. And it will mention the cost.

5. After the person pick the ride, the money is calculated and ask him to pay.

6. After he paid , The bot will generate the random code on which he can show 
   the code to ride counter as a ticket, With this he can enjoy the ride/show happily.

""" 

from morning import morg_amount
from afternoon import aft_amount
from Evening import eve_amount
from rancode_gen import rand_code

def Greetings():
    print()
    print('...**********....')
    print()
    print("Hello!   >**< Welcome to the Kiddo Amuesment Park >**<")
    print("Where you can meet the Joy and awsomness")
    print()
    choice_selection()
    return

def choice_selection():
    print(" Your Good Name :")
    Name=input()
    print()
    print(Name+", Rides are on move on the basis of timing. ")
    print()
    print("Choose which rides do you want to book for.")
    sessions=['1. Morning', '2. Afternoon', '3. Evening'] 
    print()
    
    for i in sessions:
        print(i)
    print("Please enter numericals....")
    
    choosen_integer=int(input())
    if choosen_integer==1:
        morg_amount(choosen_integer)
    elif choosen_integer==2:
        aft_amount(choosen_integer)
    elif choosen_integer==3:
        eve_amount(choosen_integer)
    else:
        print("Please check you have entered unvalid option......")
        print("Try again")
        choice_selection()


    return

def bot():
    Greetings()
    print()
    print( rand_code())
    print()

    print("wish you a safe journey")


bot()
