#PASSWORD GENERATOR
for p in range(3):
    import random
    a1=int(input('Enter length of desired Password: '))
    print('Your desired length for Password is: ',a1)
    print("Let's generate your Password!")
    ch='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#%$&'
    pwd=""
    for i in range(a1):
        pwd=pwd+random.choice(ch)
    print(pwd)
    ag=input('Would you like to try it again? (y/n)')
    if ag=='y' or ag=='Y':
        continue
    elif ag=='n' or ag=='N':
        print("Thanks for Using Password Generator!")
        break
    else:
        print('Invalid Response!')
        break



