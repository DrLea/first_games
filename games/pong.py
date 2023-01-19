from turtle import Turtle, Screen
import time
from random import randint, random

leftCounter = 0
rightCounter = 0

screen = Screen()
ball = Turtle("circle")
ball.color("white")
ball.pu()
ball.speed(0)
ball.seth(randint(1,360))
screen.setup(width=900,height=600)
screen.bgcolor("black")
screen.listen()


class ScoreBoard(Turtle):
    def __init__(self,arg,x,y):
        super().__init__()
        self.color("white")
        self.ht()
        self.pu()
        self.setpos(x,y)
        self.write( arg, move=False, align="center", font= ("Arial",20,"normal"))
    def sc(self,arg):
        self.clear()
        self.write( arg, move=False, align="center", font= ("Arial",20,"normal"))


class Padle:
    def __init__(self,x):
        self.padle = Turtle("square")
        self.padle.color("white")
        self.padle.shapesize(stretch_wid = 5, stretch_len = 1)
        self.padle.pu()
        self.padle.goto(x,0)
    def up(self):
        if self.padle.ycor()<250:
            self.padle.goto(self.padle.xcor(),self.padle.ycor()+40)
        
    def down(self):
        if self.padle.ycor()>-250:
            self.padle.goto(self.padle.xcor(),self.padle.ycor()-40)



a = Padle(400)
b = Padle(-400)
referi = Turtle()
referi.ht()
referi.color("white")
referi.pu()
referi.goto(0,-50)
referi.pd()
referi.circle(50)
referi.pu()
referi.goto(0,300)
referi.rt(90)
for i in range(30):
    referi.pd()
    referi.fd(10)
    referi.pu()
    referi.fd(10)

screen.onkey(b.up,"w")
screen.onkey(b.down,"s")
screen.onkey(a.up,"Up")
screen.onkey(a.down,"Down")

q= ScoreBoard(0,-380,270)
w= ScoreBoard(0,380,270)
while True:
    ball.fd(10)
    time.sleep(0.01)
    if ball.xcor()<-440:#left wall
        ball.seth(180-ball.heading())
        rightCounter+=1
        w.sc(rightCounter)
    elif ball.xcor()>440:#right wall
        ball.seth(180-ball.heading())
        leftCounter+=1
        q.sc(leftCounter)
    elif ball.ycor()<-280:#floor
        ball.seth(360-ball.heading())
    elif ball.ycor()>280:#ceil
        ball.seth(360-ball.heading())
    elif ball.xcor()>380 and a.padle.distance(ball)<55:
        ball.seth(180-ball.heading())
    elif ball.xcor()<-380 and b.padle.distance(ball)<55:
        ball.seth(180-ball.heading())

screen.exitonclick()



""" ceil  360-x
    left  180-x
    floor 360-x
    right 180-x
      """