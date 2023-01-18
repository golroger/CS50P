import requests
import sys


def virgule(b) :

    b=str(b)
    c="" ; t =1
    for i in range(len(b)) :
        if b[i] == "." :
            bf = b[i:len(b)]
            b=b[0:i]
            break
    for i in range(len(b)-1,-1,-1) :
        if t == 3 :
             c=c+b[i]+','
             t=1
        else :
            c=c+b[i]
            t=t+1
    c=c[::-1]
    if c[0] == "," :
        c=c[1::]
    return c+bf

while True :
    try :
        if len(sys.argv) < 2 :
            sys.exit("Missing command-line argument")
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        rate = (((response.json()['bpi'])['USD'])["rate"])
        rate = rate.replace(",","")
        b = float(rate) * float(sys.argv[1])
        b=f'{b:.4f}'
        print("$"+virgule(b))
        break
    except ValueError :
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        pass
