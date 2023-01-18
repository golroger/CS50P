import re
import sys


def main():
    print(convert(input("Hours: ")))

def convertpm(hpm, ham, minutes_pm , minutes_am , direct) :

    if direct == 0 :
        hpm = int(hpm) ; ham = int(ham)
        if  int(minutes_pm) >= 60 or int(minutes_am) >= 60 :
            raise ValueError
        elif hpm > 12 or hpm < 0 :
            raise ValueError
        elif ham > 12 or ham < 0 :
            raise ValueError
        else :
            if hpm < 12 : hpm = hpm + 12
            elif ham == 12 : ham ="00"
            hpm = str(hpm)
            if ham != 12 and ham != "00" :
                return "0"+str(ham)+ ":" + minutes_am +" to " + hpm +":"+ minutes_pm
            else :
                    return str(ham)+ ":" + minutes_am +" to " + hpm +":"+ minutes_pm
    elif direct == 1 :
        hpm = int(hpm) ; ham = int(ham)
        if  int(minutes_pm) >= 60 or int(minutes_am) >= 60 :
            raise ValueError
        elif hpm > 12 or hpm < 0 :
            raise ValueError
        elif ham > 12 or ham < 0 :
            raise ValueError
        else :
            if hpm < 12 : hpm = hpm + 12
            elif ham == 12 : ham = str("00")
            hpm = str(hpm)
            if ham != 12  and ham != "00":
                return hpm +":"+ minutes_pm  +" to " +"0"+str(ham)+ ":" + minutes_am
            else :
                    return hpm +":"+ minutes_pm +" to " + str(ham)+ ":" + minutes_am


def convert(s):
    try :
        match = re.search(r"(.+):(.+) AM to (.+):(.+) PM$",s)
        match2 = re.search(r"^(.+) AM to (.+) PM$" ,s)
        match3 = re.search(r"^(\d+) PM to (\d+) AM$" ,s)
        match4 = re.search(r"(.+):(.+) PM to (.+):(.+) AM$",s)
        if match :
            ham = match.group(1) ;minutes_am = match.group(2)
            hpm = match.group(3) ; minutes_pm = match.group(4)
            return convertpm(hpm , ham ,  minutes_pm  , minutes_am,0)
        elif match2 :
            ham = match2.group(1) ; hpm = match2.group(2)
            minutes_am ="00" ; minutes_pm = "00"
            return convertpm(hpm , ham ,  minutes_pm  , minutes_am,0)
        elif match4 :
            ham = match4.group(3) ;minutes_am = match4.group(4)
            hpm = match4.group(1) ; minutes_pm = match4.group(2)
            return convertpm(hpm , ham , minutes_pm,minutes_am,1)

        elif match3 :
            ham = match3.group(2) ; hpm = match3.group(1)
            minutes_am ="00" ; minutes_pm = "00"
            return convertpm(hpm , ham , minutes_pm,minutes_am,1)
        else :
            raise ValueError
    except ValueError :
        raise ValueError

if __name__ == "__main__":
    main()