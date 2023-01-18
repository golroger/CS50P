def convert(time):
    for i in range(len(time)) :
        if time[i] == ":" :
            h = float(time[0:i]) ; min = float(time[i+1:len(time)])
    return (h+min/60)


def main():
    x= input("what is the time :")
    cc = convert(x)

    if 7 <= cc <= 8 :
        print( "breakfast time")
    elif 12 <= cc <= 13 :
        print( "lunch time")
    elif 18 <= cc <= 19 :
        print( "dinner time")
    else :
        print( "")

if __name__ == "__main__":
    main()