import random
count = 7
def fun():
    num = random.randint(1,100)
    return num
random_num=fun()
print(random_num)
while count>=1:
    
    guess_num = int(input("guess a number: "))

    if random_num==guess_num:
        print("You WON the game")
        next=input("try again?: ")
        if next.casefold()=="yes":
            count=7
            random_num=fun()
            print(random_num)
            continue
        else:
            print("Thank you for playing")
            break

    else:
        count=count-1
        if count==0:
            print("Limit exceeds, Thank you")
            break
        else:
            if random_num>guess_num:
                print("Num is too low")
            else:
                print("Num is too high")
                continue 

