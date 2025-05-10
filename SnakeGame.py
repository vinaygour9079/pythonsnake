import turtle
import random
import time
delay=0.1
sc=0
hs=0
bodies=[]
#creating a screen
s1=turtle.Screen()
s1.title("Snake Game")
s1.bgcolor("Light Blue")
s1.setup(width=600,height=600)
#creating a head
head=turtle.Turtle()
head.shape("circle")
head.color("red")
head.fillcolor("black")
head.penup()
head.goto(0,0)
head.speed(0)
head.direction="stop"
#creating a food
food=turtle.Turtle()
food.shape("square")
food.color("pink")
food.penup()
food.ht
food.goto(200,250)
food.st()
food.speed(0)
#Scoreboard
sb=turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-280,280)
sb.write("Score:0 | Highest Score:0")
#Creating a function for moving in all directons
def moveUp():
    if head.direction!="down":
        head.direction="up"
def moveDown():
    if head.direction!="up":
        head.direction="down"
def moveRight():
    if head.direction!="left":
        head.direction="right"
def moveLeft():
    if head.direction!="right":
        head.direction="left"
def moveStop():
    head.direction="stop"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)    
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)    
#Event handling
        
s1.listen()
s1.onkey(moveUp,"Up")
s1.onkey(moveDown,"Down")
s1.onkey(moveLeft,"Left")
s1.onkey(moveRight,"Right")
s1.onkey(moveStop,"space")

#mainloop
while True:
    s1.update()
    #check collision with border
    if head.xcor()>290:
        head.setx(-290)
    if head.ycor()>290:
        head.sety(-290)
    if head.xcor()<-290:
        head.sety(290)
    if head.ycor()<-290:
        head.sety(290)
#check collision with food
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #increase size of snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color("pink")
        bodies.append(body)
        sc=sc+100
        delay=delay-0.001
        if sc>hs:
            hs=sc #update highest score
        sb.clear()
        sb.write("Score:{}  |:Highest Scoree:{}".format(sc,hs))
#move snake bodies
    for i in range(len(bodies)-1,0,-1):
      bodies[i-1].xcor()
      y=bodies[i-1].ycor()
      bodies[i].goto(x,y)
    if len(bodies)>0:
      x=head.xcor()
      y=head.ycor()
      bodies[0].goto(x,y)
    move()
#check collision with snake body
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for body in bodies:
                body.ht()
            bodies.clear()
            sc=0
            delay=0.1
            sb.clear()
            sb.write("Score:{} | Highest Score:{}".format(sc,hs))
    time.sleep(delay)    
s1.mainloop()
