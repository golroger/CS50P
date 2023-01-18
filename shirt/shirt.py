import sys as s
import csv
from PIL import Image, ImageOps

    # check the number of the cmd-line arguments
l=["jpg","png","jpeg"]
try :

        if  len(s.argv) <  3 :
            s.exit("Too few command-line arguments")

        # check the python extension of the file
        elif len(s.argv) == 3 :
            name1 = s.argv[1] ; name2 = s.argv[2]
            if (name1[len(name1)-3:len(name1)] not in l ) or (name2[len(name2)-3:len(name2)] not in l ):
                s.exit("Invalid input")
            elif name1[len(name1)-3:len(name1)] !=  name2[len(name2)-3:len(name2)] :
                s.exit("Input and output have different extensions")
        # if everything is ok, let have read the file
            else :
                # the work of the program : if everything is okay
                shirt =Image.open("shirt.png")
                w,h = shirt.size
                im= Image.open(s.argv[1])
                im3 = ImageOps.fit(im, (w,h)) # crop
                im3.paste(shirt, shirt)
                im3.save(s.argv[2])

        elif len(s.argv) > 3 :
            s.exit("Too many command-line arguments")
except FileNotFoundError :
       s.exit("Could not read "+ s.argv[1])
