def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def test(s) :
    h = ""
    for i in range(len(s)) :
        if s[i].isnumeric() :
            h = s[i-1:len(s)]
    return h

def is_valid(s):
    aa=""
    nn = ""
    dd= ""
    l=[]
    for i in range( len(s)) :
        if s[i].isalpha() :
            aa = aa + s[i]
        elif s[i].isnumeric() :
            nn = nn + s[i]
        else :
            dd =dd + s[i]
    l.append(aa) ; l.append(nn) ; l.append(dd)
    # test begin
    if len(s) > 6 or len(s) < 2 :

        return False
    elif s[0:2].isalpha() == False :

        return False
    elif len(l[2]) !=0 :

        return False
    elif len(l[0]) == 0 :

        return False
    if len(test(s)) > 0 :
        if test(s)[0] == "0" :

            return False
        elif test(s).isnumeric() == False :
            return False
        else :
            return True
    else :
        return True

if __name__ == "__main__":
    main()