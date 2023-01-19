from turtle import Turtle, Screen
import random

colors = ["red","orange","yellow","green","cyan","blue","purple"]
go = False
s = Screen()
s.setup(width=1200,height=700)
bet = s.textinput(title="Bet", prompt="Make your bet: ")
players = []
for i in colors:
    players.append(Turtle(shape="turtle"))
    players[len(players)-1].color(i)

y = 120
for i in players:
    i.setpos(-550,y)
    y-=40

for i in players:
    i.clear()

referi = Turtle(visible=False)
referi.pu()
referi.goto(550,-300)
referi.pd()
referi.pensize(30)
referi.goto(550,300)
del referi

if bet:
    go = True

while go:
    for i in players:
        i.fd(random.randint(0,10))
        if i.pos()[0]>550:
            go = False
            s.textinput(title="winner", prompt=f"{i.color()}")

s.exitonclick()  