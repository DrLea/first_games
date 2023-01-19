from itertools import count
import os
import random
hangman = []

def start():
    r1 = [' ','+','-','-','-','+',' ']
    r2 = [' ','|',' ',' ',' ','|',' ']
    r3 = [' ','|',' ',' ',' ','O',' ']
    r4 = [' ','|',' ',' ','/','|','\\']
    r5 = [' ','|',' ',' ',' ','|',' ']
    r6 = [' ','|',' ',' ','/',' ','\\']
    r7 = ['=','=','=',' ',' ',' ',' ']

    hangman = [r1,r2,r3,r4,r5,r6,r7]
    for i in hangman:
        for j in i:
            print(j, end="")
        print("")


def select(a):
    global change, life
    count = -1
    for i in word:
        count+=1
        if i.lower() == a.lower():
            desk[count]=i
            change = True
    if not change:
        life-=1
    else:
        if '_' not in desk:
            print("Victory!")
            life = 0
        change = False
    
            

start()
print("HANGMAN")
input("Shall we start now?")
os.system('cls')

words = ["Lambda", "Boobs", "AAA"]
word = random.choice(words)
desk = []
chosen = []
change = False
life = 8
for i in word:
    desk += '_'

while life:
    print(f"life: {life}")
    for i in desk:
        print(f" {i} ", end="")
    choise = input("\nGuess the letter: ")
    os.system('cls')
    if choise not in chosen:
        chosen += choise
        select(choise)
    else:
        print("It was already chosen")

start()
print(f"The word was {word}")
print("Game Over")
input()
