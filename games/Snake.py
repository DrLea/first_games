import time
from turtle import Turtle, Screen
import random

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

SPEED = 1

screen = Screen()
if screen:
    screen.setup(600,600)
    screen.bgcolor("black")
    screen.tracer(False)
    screen.listen()

screen.onkeypress(lambda: a.snake[0].seth(LEFT) if a.snake[0].heading()!=LEFT and a.snake[0].heading()!=RIGHT else LEFT,"a")
screen.onkeypress(lambda: a.snake[0].seth(RIGHT) if a.snake[0].heading()!=RIGHT and a.snake[0].heading()!=LEFT else LEFT,"d")
screen.onkeypress(lambda: a.snake[0].seth(UP) if a.snake[0].heading()!=UP and a.snake[0].heading()!=DOWN else LEFT,"w")
screen.onkeypress(lambda: a.snake[0].seth(DOWN) if a.snake[0].heading()!=DOWN and a.snake[0].heading()!=UP else LEFT, "s")

t = Turtle()
cherry = Turtle()
cherryCounter = 0
score = 0
game = True


class ScoreBoard(Turtle):
    def __init__(self,arg):
        super().__init__()
        self.color("white")
        self.ht()
        self.pu()
        self.setpos(0,260)
        self.write(f"Score: {arg}", move=False, align="center", font= ("Arial",20,"normal"))
    def sc(self,arg):
        self.clear()
        self.write(f"Score: {arg}", move=False, align="center", font= ("Arial",20,"normal"))

def makeCherry():
    global cherryCounter, cherry
    if not cherryCounter:
        del cherry
        cherry = Turtle("circle")
        cherry.color("red")
        cherry.pu()
        cherry.goto(random.randint(-280,280),random.randint(-280,280))
        cherryCounter+=1
        


class Snake:
    def __init__(self,x = 0, y = 0):
        self.snake = []
        # self.moves = [0,0,0]
        self.snake += [Turtle(shape="square"),]
        self.snake += [Turtle(shape="square"),]
        self.snake += [Turtle(shape="square"),]
        for i in self.snake:
            i.pu()
            i.color("white")
            i.speed(1)
        self.snake[1].setpos(x,y)        
        self.snake[2].setpos(x-15,y)
        self.snake[0].setpos(x+15,y)
    
    def action(self):
        global game
        length = len(self.snake)-1
        for i in range(length,0,-1):
            self.snake[i].setpos(self.snake[i-1].pos())
        self.snake[0].fd(15)
        if self.snake[0].xcor()>300:
            self.snake[0].setpos(-300,self.snake[0].ycor())
        elif self.snake[0].xcor()<-300:
            self.snake[0].setpos(300,self.snake[0].ycor())
        elif self.snake[0].ycor()>300:
            self.snake[0].setpos(self.snake[0].xcor(),-300)
        elif self.snake[0].ycor()<-300:
            self.snake[0].setpos(self.snake[0].xcor(),300)
        for i in self.snake[1:]:
            if self.snake[0].distance(i)<15:
                game = False
                t.color("white")
                t.pd()
                t.write("Game Over", move=False, align="center", font= ("Arial",20,"normal"))

        # x,y = self.snake[0].pos()
        # for i in range(1,len(self.snake)):
        #     xi,yi = self.snake[i].pos()
        #     if abs(abs(x)-abs(xi))<10 and abs(abs(y)-abs(yi))<10:
        #         print("Game Over")
        screen.update()
        time.sleep(1/(5*SPEED))

    
    def add(self):
        global cherry, cherryCounter,score
        # x,y = self.snake[0].pos()
        # xc,yc = cherry.pos()
        # if  abs(abs(x)-abs(xc))<10 and abs(abs(y)-abs(yc))<10:
        if self.snake[0].distance(cherry)<20:
            cherry.ht()
            cherry.clear()
            cherryCounter-=1
            newseg = Turtle("square")
            newseg.color("white")
            newseg.pu()
            self.snake.append(newseg)
            score+=1
            s.sc(score)
            
            


if 0:
    # def push(self, arg):
    #     self.moves.reverse()
    #     if len(self.moves)>len(self.snake):
    #         self.moves.pop(0)
    #     self.moves.append(arg)
    #     self.moves.reverse()

    # def left(self):
    #     self.push(-1)
    # def right(self):
    #     self.push(1)
    # def move(self):
    #     self.push(0)

    # def action(self):
    #     for i in range(len(self.snake)):
    #         if not self.moves[i]:
    #             self.snake[i].fd(15)
    #         elif self.moves[i]==-1:
    #             self.snake[i].lt(90)
    #         else:
    #             self.snake[i].rt(90)
    #     screen.update()
    #     time.sleep(1/(5*SPEED))
    #     self.move()

    

    # def move(self):
    #     time.sleep(1/(5*SPEED))
    #     for i in self.snake:
    #         i.fd(15)
    #     screen.update()
    
    # def left(self):
    #     for i in self.snake:
    #         i.lt(90)
    #         for i in self.snake:
    #             i.fd(15)
    #         screen.update()
    #         time.sleep(1/(5*SPEED))
    
    # def right(self):
    #     for i in self.snake:
    #         i.rt(90)
    #         for i in self.snake:
    #             i.fd(15)
    #         screen.update()
    #         time.sleep(1/(5*SPEED))
    pass


a = Snake(30,50)
s = ScoreBoard(score)
while game:
    makeCherry()
    a.action()
    a.add()
    






screen.exitonclick()