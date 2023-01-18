import random as rd


while True :
    try :
        level = input("Level :")
        if int(level) <= 0 :
            level = input("Level :")
    except TypeError :
        level = input("Level :")
    except ValueError :
        level = input("Level :")
    else :
        break

n = rd.randint(1,int(level))

while True :
    try :
        g = input("Guess :")
        g=int(g)
        if g < n :
            print("Too small!")
        elif g > n :
            print("Too large!")
        elif g == n:
            print("Just right!")
            break
        elif g < 0 :
            g = input("Guess :")
    except ValueError :
        g = input("Guess :")
    except TypeError :
        g = input("Guess :")
    
