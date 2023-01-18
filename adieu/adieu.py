n=""
names = []
while True :
    try :
        x = input("Name :")
        names.append(x)
    except EOFError :
        break

if len(names) == 1 :
    print("Adieu, adieu, to "+ names[0])
elif len(names) == 2 :
    print("Adieu, adieu, to "+ names[0] + " and " + names[1])
elif len(names) > 2 :
    for i in range(len(names)) :
        if i  != len(names) - 1 :
            n = n + names[i]+ ", "
        elif i == len(names)-1 :
            n= n + "and " + names[i]
    print("Adieu, adieu, to "+n)
