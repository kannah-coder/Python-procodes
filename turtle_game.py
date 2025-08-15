import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS=["red",'pink','black','blue','orange','cyan','brown','yellow','purple','green']



def get_number_of_racer():
    racers=0
    while True:
        racers=input("Enter the number of racers(2-10): ")
        if racers.isdigit():
            racers=int(racers)
        else:
            print("Input is not numeric ...Try agian!!")
            continue

            # if ou write somthing here it wont run as continue is present it goes to start of the loop

        if(2<=racers<=10):
            return racers
        else:
            print("NOT in range..Try again!!")

def race(colors):
    turtles=create_turtles(colors)
    while True:
        for racer in turtles:
            distance=random.randrange(1,20)
            racer.forward(distance)
            x,y=racer.pos()
            if y >= HEIGHT//2-10:
                return colors[turtles.index(racer)]
def create_turtles(colors):
    turtles=[]
    spacingx=WIDTH // (len(colors)+1)
    for i,color in enumerate(colors):

        racer=turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+(i+1)*spacingx,-HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)
    return turtles
def init_turtle():
    WIDTH, HEIGHT = 500, 500
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")

racers=get_number_of_racer()
init_turtle()
random.shuffle(COLORS)
colors=COLORS[:racers]


winner=race(colors)
print(winner)
print("THe winner is the turtle with color:",winner)
time.sleep(6)
turtle.done()




# racer=turtle.Turtle()
# racer.speed(1)
# racer.penup()
# racer.shape('turtle')
# racer.color('cyan')
# racer.forward(100)
# racer.left(90)
# racer.pendown()
# racer.backward(100)
# racer.forward(100)
# racer.pendown()
# racer.left(100)
#
# racer2=turtle.Turtle()
# racer2.speed(1)
# racer2.penup()
# racer2.shape('turtle')
# racer2.color('cyan')
# racer2.forward(100)
# racer2.left(90)
# racer2.pendown()
# racer2.backward(100)
# racer2.forward(100)
# racer2.pendown()
# racer2.left(100)

