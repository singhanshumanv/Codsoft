#CALCULATOR
for i in range(1,3):
    a=int(input("Enter First Number : "))
    op=input("Please choose operator (+,-,*,/,^) ")
    b=int(input("Enter Second Number : "))
    if op=='+':
         add=a+b
         print("You have chosen Addition & the Addition is  : ",add)
    elif op=='-':
        sub=a-b
        print("You have chosen Subtraction & the Subtraction is  : ",sub)
    elif op=='*':
        mul=a*b
        print("You have chosen Multiplication & the Multiplication is  : ",mul)
    elif op=='/':
        if b!=0:
            div=a/b
            print("You have chosen Division & the Division is  : ",div)
        else :
            print("Invalid Operand!")
    elif op=='^':
        po=a**b
        print("You have chosen raising power & evaluation is  : ",po)
    else :
        print("Invalid Operator!")
    c=input("Would you like to use calculator again ? (reply with Y or N) ")
    if c=='Y' or c=='y':
        continue
    elif c=='N' or c=='n':
        print("Thanks for using !")
        break
    else :
        print("Invalid response")
        break
    
        
