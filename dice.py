import random
c=0
while True:
    d=int(input("Want to play? Yes(1)_No(0): "))
    if d==1:
        a=int(input("Enter a number between 1-6: "))
        b=random.randint(1,6)
        if a>=1 and a<=6:
            if a==b:
                c+=1
            else:
                pass
            print(f"Computer got: {b}")
            print(f"Your score is: {c}")
            print()
        else:
            print("Invalid Input")
            break
    elif d==0:
        print("You Quit")
        print(f"Your total score is : {c}")
        break
    else:
        print("Invalid Input")
        break
