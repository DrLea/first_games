from turtle import Turtle, Screen, colormode
import time
from random import randint

speed = 0.2

screen = Screen()
screen.setup(width=600,height=600)
screen.listen()
screen.tracer(0)

class Car(Turtle):
    def __init__(self, y):
        super().__init__("square", visible=False)
        self.shapesize(stretch_len=2, stretch_wid=1)
        colormode(255)
        self.color((randint(1,255),randint(1,255),randint(1,255)))
        self.pu()
        self.speed(0)
        self.goto(300,y*60)
        self.showturtle()
    def collision(self):
        global game
        if self.distance(a)<20:
            score.clear()
            score.goto(0,0)
            score.write(f"Game Over score: {level}",False,"center",("Roman",20,"normal"))
            game = False


a = Turtle("turtle")
score = Turtle(visible=False)
score.pu()
level = 1
game = True
score.goto(260,260)
score.write(level,False,"center",("Roman",20,"normal"))
cars = []
a.pu()

def go():
    for car in cars:
        car.goto(car.xcor()-20,car.ycor())
        car.collision()
        if car.xcor()<-350:
            cars.remove(car)
            car.ht()
            del car
    screen.update()


def start():
    a.speed(0)
    a.goto(0,-280)
    a.seth(90)
    a.speed(10)


screen.onkeypress(lambda: a.fd(30),"space")

start()
while game:
    cars.append(Car(randint(-4,4)))
    go()
    time.sleep(speed)
    if a.ycor()>=290:
        for car in cars:
            car.ht()
            del car
        cars.clear()
        start()
        speed *= 0.9
        level+=1
        score.clear()
        score.write(level,False,"center",("Roman",20,"normal"))





screen.exitonclick()