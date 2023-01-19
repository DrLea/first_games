from random import randint
logo = ''' 
 .---. .-. .-..----. .----. .----.   .-. .-..-. .-..-.   .-..----. .----..----. 
/   __}| { } || {_  { {__  { {__     |  `| || { } ||  `.'  || {}  }| {_  | {}  }
\  {_ }| {_} || {__ .-._} }.-._} }   | |\  || {_} || |\ /| || {}  }| {__ | .-. \\
 `---' `-----'`----'`----' `----'    `-' `-'`-----'`-' ` `-'`----' `----'`-' `-'
 '''
print(logo)
while True:
    diff = input("Please choose the the difficulty (E)asy or (H)ard: ").upper()
    if diff == 'H':
        close = 2
        medi = 3
        far = 5
        life = 5
        break
    elif diff == "E":
        close = 3
        medi = 10
        far = 20
        life = 10
        break
    else:
        print("wrong input")
number = randint(1,100)
print("Guess the number from 1 to 100")

while True:
    choise = int(input(f"life: {life}  choose a number: "))
    if abs(number-choise)>far:
        print("very ", end="")
    elif abs(number-choise)>medi:
        print("merely ", end="")
    elif abs(number-choise)>close:
        print("a bit ", end="")
    if number - choise > 0:
        print("low")
    elif number - choise < 0:
        print("high")
    else:
        print(f"You got it number was {number}")
        break
    life-=1
    if life==0:
        print(f"You lose number was {number}")