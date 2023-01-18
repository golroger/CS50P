try :
    fract =input("fractions :")
    for i in range(len(fract)) :
        if fract[i] == "/" :

            x = int(fract[0:i])

            y = int( fract[i+1: len(fract)])
            xx = x /y
            if xx > 1 :
                fract =input("fractions :")
            per = xx*100
            break
        elif i == len(fract) and fract[i] != "/" :

            fract =input("fractions :")
        elif fract[i].isnumeric() == False and fract[i] !="/" :
            fract =input("fractions :")

except ValueError :
    fract =int(input("fractions :"))
except ZeroDivisionError :
    fract =int(input("fractions :"))

else :
    if per == 100 or per >= 99 :
        print("F")
    elif per == 0 or per <= 1 :
        print("E")
    else :
        print(f"{per:2.0f}%")
