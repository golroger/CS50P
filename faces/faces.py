def convert(x) :
    cc = x.replace(":(","🙁")
    cc = cc.replace (":)" , "🙂")
    return cc

def main() :
    user = input("insert you msg : ")
    print(convert(user))

main()