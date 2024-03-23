#GAME OF ROCK,PAPER & SCISSOR
for i in range(3):
    import random
    print("Welcome to the Game of Rock, Paper & Scissor!")
    print("Choice instructions:-\n1.Use R for Rock\n2.Use P for Paper\n3.Use S for Scissor")
    print("Your turn to give your choice!")
    a=input("Enter your Choice: ")
    if a=='R':
        print("Your choice is Rock")
    elif a=='P':
        print("Your choice is Paper")
    elif a=='S':
        print("Your choice is Scissor")
    else:
        print("Invalid choice!")
    print("Now it's turn for Computers choice!")
    ch='xyz'
    comch=random.choice(ch)
    if comch=='x':
        print("Computer's choice is Rock")
    elif comch=='y':
        print("Computer's choice is Paper")
    elif comch=='z':
        print("Computer's choice is Scissor")
    if a=='R' and comch=='z':
        print('You won!')
        print("Your Score-1\nComputer's score-0")
    elif a=='S' and comch=='x':
        print('Computer won!')
        print("Your Score-0\nComputer's score-1")
    elif a=='S' and comch=='y':
        print('You won!')
        print("Your Score-1\nComputer's score-0")
    elif a=='P' and comch=='z':
        print('Computer won!')
        print("Your Score-0\nComputer's score-1")
    elif a=='P' and comch=='x':
        print('You won!')
        print("Your Score-1\nComputer's score-0")
    elif a=='R' and comch=='y':
        print('Computer won!')
        print("Your Score-0\nComputer's score-1")
    elif a=='R' and comch=='x':
        print("It's a Tie!")
    elif a=='P' and comch=='y':
        print("It's a Tie!")
    elif a=='S' and comch=='z':
        print("It's a Tie!")
    b=input("Would you like to Play again? (y/n) ")
    if b=='y' or b=='Y':
        continue
        print("Well Played!")
    else:
        print("Well Played!")
        break


        
        
        
        
        
    
    
    
