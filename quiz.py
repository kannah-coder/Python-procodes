print("welcome to the quiz")

playing=input("Do you wanna play this game ? ")

if (playing.lower())!="yes":
    print("ok quited")
    quit()

print("okay lets play :)")
score=0
answer=input("what does cpu stands for? ")
if answer.lower()=="central processing unit":
    print("yeah you are correct!")
    score+=1
print("oops incorrect, Try again ")
answer=input("what does gpu stands for? ")
if answer.lower()=="graphics processing unit":
    print("yeah you are correct!")
    score+=1
print("oops incorrect, Try again ")

print("you got " + str(score) +" questions correct!")


