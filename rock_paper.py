import random

user_wins=0
computer_wins=0
lst=["Rock","Paper","Scissor"]
while True:
    a=input("choose rock/paper/scissor or Q for quit: ")
    if a.lower()=="q":
        print("successfully existed")
        break
    if a.capitalize() not in lst:
        print("please reenter correct one ")
        continue
    random_number=random.randint(0,2)
    # rock=0,paper=1,scissor=2
    computer_pick=lst[random_number]
    print("Computer picks: " ,lst[random_number] )

    if a.lower()=="rock" and computer_pick.lower()=="paper":
        computer_wins+=1
        print("computer wins")

    elif a.lower()=="paper" and computer_pick.lower()=="scissor":
        computer_wins+=1
        print("computer wins")

    elif a.lower()=="scissor" and computer_pick.lower()=="rock":
        computer_wins+=1
        print("computer wins")
    elif a.lower()==computer_pick:
        print("oops both are same try again")

    else:
        user_wins+=1
        print("You won!")

print("Your Total Score: " , user_wins)
print("computer score: ",computer_wins)
