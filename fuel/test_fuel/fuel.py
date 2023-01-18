def main():
    frac  =input("fractions :")
    d = convert(frac)
    print(gauge(d))


def convert(fract):
    try :
        for i in range(len(fract)) :
            if fract[i] == "/" :
                        x = int(fract[0:i])
                        y = int( fract[i+1: len(fract)])
                        per = (x/y)*100
                        return int(per)
        if x/y > 1 :
                        raise Exception(ValueError)

    except ValueError :
            raise ValueError
    except ZeroDivisionError :
        raise ZeroDivisionError


def gauge(dd):
    if  dd <= 1 :
        return  "E"
    elif dd >=  99 :
        return "F"
    else :
        return (str(dd)+"%")

if __name__ == "__main__":
    main()
