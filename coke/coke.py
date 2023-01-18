due = 50
print("Amount due :",due)
L= [5,10,25,50]

cond = True
while cond :
    owed = input("insert coin : ")
    if int(owed) in L : due = due - int(owed)
    if due <= 0 :
        print("Change owed:", (-1)*due)d
        break
    elif int(owed) in L :

        print("Amount due :",due)

    elif int(owed) not in L :
        print("Amount due :",due)


