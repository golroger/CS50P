cc = input(" put the expression :")
cc=cc.replace(" ","")

l=["-","+","/","*"]

for i in range(len(cc)) :
    if cc[i] in l :
        op = cc[i]
        x=float(cc[0:i]) ; y = float(cc[i+1:len(cc)])

match op :
    case "-" :
        print("%.1f" % (x-y))
    case "+" :
        print("%.1f" % (x+y))
    case "/" :
        print("%.1f" % (x/y))
    case "*" :
        print("%.1f" % (x*y))



