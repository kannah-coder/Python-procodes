name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road. It has come to an end and you can go left or right. Which way would you like to go? (left/right): ").lower()

if answer == "left":
    answer = input("You come to a river. You can walk around it or swim across. Type 'walk' to walk or 'swim' to swim: ").lower()

    if answer == "swim":
        print("You swam across the river and were eaten by alligators. You lose. :( ")
    elif answer == "walk":
        print("You walked for many miles, ran out of water, and lost the game. :( ")
    else:
        print("Not a valid option. You lose. :( ")

elif answer == "right":
    answer = input("You come to a bridge. It looks wobbly. Do you want to cross it or head back? (cross/back): ").lower()

    if answer == "back":
        print("You go back and lose the opportunity. You lose. :( ")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to him? (yes/no): ").lower()

        if answer == "yes":
            print("You talk to the stranger, and he gives you a diamond. You won! :) ")
        elif answer == "no":
            print("You ignored the stranger, and he kills you. You lose. :( ")
        else:
            print("Not a valid option. You lose. :( ")
    else:
        print("Not a valid option. You lose. :( ")

else:
    print("Not a valid option. You lose. :( ")
