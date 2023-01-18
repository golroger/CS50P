import sys as s
from pyfiglet import Figlet
from random import choice

fonts = ["rectangles","slant","acrobatic","alligator","alligator2","alphabet","avatar","banner","banner3-D","banner3","banner4","barbwire","basic","bell","bigchief","binary","block","bubble","bulbhead","calgphy2","caligraphy","catwalk","chunky","coinstak","colossal","computer","contessa","contrast","eftichess","eftipiti","eftirobot","eftitalic"]

if len(s.argv) == 1 :
    x =input("Input :")
    f = Figlet(font=choice(fonts))
    print(f.renderText(x))
elif len(s.argv) == 3 :
    if (s.argv[1] == "-f" or s.argv[1] == "--font" ) and (s.argv[2] in fonts ):
        x =input("Input :")
        f = Figlet(font=s.argv[2])
        print(f.renderText(x))
    else :
        s.exit("Invalid usage")
else :
    s.exit("Invalid usage")




