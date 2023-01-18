#Golroger
from datetime import date
import inflect as inf # turn numbers to words
import sys
import re

p = inf.engine() # turn numbers to words

def main():
    x=input("Date of Birth: ")
    print(convert_minutes(is_valid(x)))
# this function check the validity of the date entred, using regex. if the date is valid it return it in a list
# the first element of the list is boolean : TRUE OR FALSE
def is_valid(s) :
    l=[]
    match = re.search("^([0-9][0-9][0-9][0-9])-([0-9][0-9])-([0-9][0-9])$",s)
    if match :
        year = match.group(1)
        month = match.group(2)
        day= match.group(3)

        if int(day) > 31 or int(day)  == 0 or int(month) > 12 or int(month)  == 0 or int(year) == 0:
             l.append(False)
             return l
        l.append(True) ; l.append(year) ; l.append(month) ; l.append(day)
        return l
    else :
        l.append(False)
        return l
# this function convert the diffrence of days to minutes using date module
def convert_minutes(l) :
    try :
        if l[0] :
            noun = [] ; nouns = ""
            year = int(l[1]) ; month = int(l[2]) ; day = int(l[3])
            birthdate = date(year,month,day)
            delta = date.today() - birthdate
            minutes = delta.days * 24 * 60
            noun= p.number_to_words(minutes , wantlist=True) # return list of words ( line 7 )
            # to remove "and"
            for j in range(len(noun)) :
                if " and " in noun[j] :
                    noun[j]= noun[j].replace(" and "," ")
            # to add "," comma
            for i in range(len(noun)) :
                if i==0 :
                    nouns =noun[i].capitalize() + ", "
                elif i != len(noun)-1 and i!=0 :
                    nouns =  nouns + noun[i] +", "
                elif i == len(noun) -1 :
                    nouns = nouns + noun[i] + " minutes"
            return nouns
        # the first element is false if is not True so the date is invalid
        else :
            sys.exit("Invalid date")
    except ValueError :
        sys.exit()

if __name__ == "__main__":
    main()