def main():
    x = input( "greeting : ")
    d = valeur(x)
    print("$"+str(d))


def valeur(greeting) :
    x = x.lower()
    x=x.replace(" ","")
    g = x[0:5]

    if g == "hello" :
        return 0
    elif g[0] == "h" :
        return 20
    else :
        return 100

if __name__ == "__main__":
         main()
