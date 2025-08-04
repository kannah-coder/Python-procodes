import random

top_of_range=input("type a number :")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print('please type larger number')
        quit()
else:
    print('please type number ')
    quit()
#a=random.randrange(11) # it doesnot include 11
a=random.randint(0,top_of_range) #it include the max range
# print(a) #to become hacker in number guessing game:)
guess=0
while True:
    guess+=1
    user_guess=input("make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)

    else:
        print('please type number ')
        continue

    if user_guess==a:
        print("you got it")
        break
    else:
        if user_guess>a:
            print("you are above the gueesed number")
        else:
            print("you are below the guessed number")
print("you got it in ",guess,"guesses")