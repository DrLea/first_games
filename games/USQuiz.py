import pandas as pd
from turtle import Screen,Turtle, mainloop,onscreenclick



def closest(x,y):
    counter = 0
    closest = 600
    cloid = 0
    clotur = 0
    for i in answers:
        key = i.distance(x,y)
        if key<closest:
            closest = key
            cloid = counter
            clotur = i
        counter+=1
    clotur.pencolor("black")
    clotur.ht()
    clotur.write(states[cloid],False,"center",("Roman",10,"normal"))


df = pd.read_csv("50_states.csv")
states = list(df.state)
xs = list(df.x)
ys = list(df.y)
answers = []
img = "blank_states_img.gif"
s = Screen()
s.setup(width=700,height=500)
s.addshape(img)
t = Turtle(img)
for i in zip(xs,ys):
    new = Turtle("circle",visible=False)
    new.shapesize(stretch_len=0.2, stretch_wid=0.2)
    new.speed(0)
    new.goto(i)
    answers.append(new)
for i in answers:
    i.clear()
    i.color("red")
    i.showturtle()

onscreenclick(closest)
mainloop()

