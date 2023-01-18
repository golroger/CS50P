month =["January","February","March","April","May","June","July","August","September","October","November","December"]

def get_date(d) :
    da =[]
    da2 = []
    g=0
    gg = 0 ; d=d.replace(" ","")
    m="" ; day = "" ; y = ""
    if d[0].isalpha() :
        for i in range(len(d)) :
            if d[i].isalpha() == True :
                m=m+d[i]
            elif d[i].isnumeric()== True and gg == 0:
                day = day + d[i]
            elif d[i] =="," :
                gg = 10
                y = d[i+1 : len(d)]

        da.append(1) ; da.append(y) ; da.append(m) ; da.append(day)
        return da
    elif d[0].isnumeric() :
        yy=""; mm="" ; dd = "" ; temp = 0
        for j in range(len(d)) :
            if d[j] == "/" and g == 0 :
                mm = d[0:j]
                temp = j
                g=1
            elif d[j] == "/" and g==1 :
                dd = d[temp+1:j]
                yy = d[j+1:len(d)]
        da2.append(2) ; da2.append(yy) ; da2.append(mm) ; da2.append(dd)
        return da2
    else :
        da3 = []
        da3.append(3)
        return da3




# ["type of date ", year , month , day]

def valid(d,month) :
    if d[0] == 1 :
        if d[2] not in month :
            return False
        elif int(d[3]) > 31 :
            return False
        else :
            return True

    elif d[0] == 2 :
        if int(d[2]) > 12 or int(d[2]) < 0 :
            return False
        elif int(d[3]) > 31 :
            return False
        else :
            return True
    elif d[0] == 3 :
        return False


# get the result of the get date function
# first reprt : ["type" , year ,"month" , day ]
def transform(d,month) :

    if d[0] == 1 :
        mm = month.index(d[2]) + 1
        yyyy = d[1]
        dd = d[3]
        if mm < 10 :
            mm = '0'+ str(mm)
        if int(dd) < 10 :
            dd = '0'+dd

        ss = yyyy + "-" + str(mm) + "-" + dd
        return ss

    elif d[0] == 2 :
        mm = d[2] # month
        dd = d[3]  # days
        if int(d[2]) < 10 : # adding '0' to month < 10
            mm = '0' + mm
        if int(d[3]) < 10 :  # adding "0" to days < 10
            dd = '0' + dd
        return d[1] + "-" + mm + "-" + dd


while True :
    try :
         date = input("Date :")
         d=get_date(date)
         if valid(d,month) :
            print(transform(d,month))
            break
    except ValueError :
        pass
    except EOFError :
            break

