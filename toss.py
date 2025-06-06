import random



def tossFunc():
    choiceT = input("press O for odds or E for evens:")
    choiceT = choiceT.upper()  # Fixed: added parentheses and assignment
    toss = int(input("enter a number from 1-6 for toss:"))
    t = random.randint(1, 6)
    
    if choiceT == "O":
        print("your choice is odd")
        
    elif choiceT == "E":
        print("your choice is even")
        
    print("the number you choosed is ", toss, " and the number choosed by the bot is ", t)
    x = toss + t
    print("the output is", x)
    
    # Initialize choice variable to prevent UnboundLocalError
    choice = ""
    
    if x % 2 == 0:
        print("the number is even")
        if choiceT == "E":
            choice = input("you won the toss press B for batting or F for fielding:")
            choice = choice.upper()  # Fixed: added parentheses and assignment
            if choice == "B":
                print("you won the toss and choosed to bat first!!!")
            elif choice == "F":
                print("you won the toss and choosed to field first!!!")
            else:
                print("invalid choice")
                choice = "B"  # Default choice if invalid input
                
        elif choiceT == "O":
            c = random.randint(1, 2)
            if c == 1:
                choice = "F"
                print("The bot won the toss and choosed to bat first you are fielding!!!")
            elif c == 2:
                choice = "B"
                print("The bot won the toss and choosed to field first you are batting!!!")
            else:
                print("invalid choice")
                choice = "B"  # Default choice if something goes wrong
                
        else:
            print("invalid choice")
            choice = "B"  # Default choice if invalid input
            
    elif x % 2 != 0:
        print("the number is odd")
        if choiceT == "O":
            choice = input("you won the toss press B for batting or F for fielding:")
            choice = choice.upper()  # Fixed: added parentheses and assignment
            if choice == "B":
                print("you won the toss and choosed to bat first!!!")
            elif choice == "F":
                print("you won the toss and choosed to field first!!!")
            else:
                print("invalid choice")
                choice = "B"  # Default choice if invalid input
                
        elif choiceT == "E":
            c = random.randint(1, 2)
            if c == 1:
                choice = "F"
                print("The bot won the toss and choosed to bat first you are fielding!!!")
            elif c == 2:
                choice = "B"
                print("The bot won the toss and choosed to field first you are batting!!!")
            else:
                print("invalid choice")
                choice = "B"  # Default choice if something goes wrong
                
        else:
            print("invalid choice")
            choice = "B"  # Default choice if invalid input
            
    return choice


def batting():
    score=0
    

choice=tossFunc()
choice.upper
print(choice)

run=0
botr=0
target=0
bott=0

if choice=="B":
    q=0
    p=0
    while q==0:
        bat=int(input("enter a number from 1 to 6 to score run : "))
        botball=random.randint(1,6)
        if bat<=0 or bat>=7:
            print("invalid number!!! Choose a number from 1 to 6")
        elif bat==botball:
            print("the number you choosed was=",bat," the number choosed by the bot was=",botball)
            print("Oh no you are out !!!")
            print("your final score is",run)
            bott=run+1
            print("you have to defend ",bott," runs")
            break
        else:
            run=run+bat
            print("the number you choosed was=",bat," the number choosed by the bot was=",botball)
            print("your run is : ",run)
            
    while p==0:
        ball=int(input("enter a number from 1 to 6 to ball : "))
        botbat=random.randint(1,6)
        if ball<=0 or ball>=7:
            print("invalid number!!! Choose a number from 1 to 6")
        elif ball==botbat:
            print("the number you choosed was=",ball," the number choosed by the bot was=",botbat)
            print("You made the bot out !!!")
            print("Bots final score is",botr)
            print("you won by ",bott-1," runs")
            break
        else:
            botr=botr+botbat
            bott=bott-botbat
            print("the number you choosed was=",ball," the number choosed by the bot was=",botbat)
            print("bots run is : ",botr)
            print("runs left to defend is ",bott," runs")
            if bott<=0:
                print("Oh no the bot won!!! Better luck next time")
                break
                
if choice=="F":
    q=0
    p=0
    while q==0:
        ball=int(input("enter a number from 1 to 6 to ball : "))
        botbat=random.randint(1,6)
        if ball<=0 or ball>=7:
            print("invalid number!!! Choose a number from 1 to 6")
        elif botbat==ball:
            print("the number you choosed was=",ball," the number choosed by the bot was=",botbat)
            print("You made the bot out !!!")
            print("the bots final score is",botr)
            target=botr+1
            print("you have to score ",target," runs")
            break
        else:
            botr=botr+botbat
            print("the number you choosed was=",ball," the number choosed by the bot was=",botbat)
            print("bot's run is : ",botr)
            
    while p==0:
        bat=int(input("enter a number from 1 to 6 to score run : "))
        botball=random.randint(1,6)
        if bat<=0 or bat>=7:
            print("invalid number!!! Choose a number from 1 to 6")
        elif bat==botball:
            print("the number you choosed was=",bat," the number choosed by the bot was=",botball)
            print("Oh no you got out !!!")
            print("your final score is",run)
            print("oh no!!! bot won by ",target-1," runs")
            break
        else:
            run=run+bat
            target=target-bat
            print("the number you choosed was=",bat," the number choosed by the bot was=",botball)
            print("your run is : ",run)
            print("runs left to defend is ",target," runs")
            if target<=0:
                print("You won!!! Congrats")
                break





