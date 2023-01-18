import time

def calcul(l) :

    d = dict()
    for i in l :
        h=0
        for j in l :
            if i == j :
                h=h+1
            d[i]= h
    return d

d=dict()
l=[]

while True :
    try :
        item = input()
        item = item.lower()
        l.append(item)

    except EOFError :
        break

d = calcul(l)
for i in sorted(d.keys()) :
    print(  d[i],i.upper())
