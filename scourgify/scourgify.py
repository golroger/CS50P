import sys as s
import csv
    # check the number of the cmd-line arguments
try :

        if  len(s.argv) <  3 :
            s.exit("Too few command-line arguments")

        # check the python extension of the file
        elif len(s.argv) == 3 :
            name = s.argv[1]
            if name[len(name)-3:len(name)] != "csv" :
                s.exit("Not a CSV file")
        # if everything is ok, let have read the file
            else :
                name = s.argv[1] ;line = []
                with open(s.argv[1],'r') as file :
                    reader = csv.DictReader(file)
                    for row in reader :
                        line.append({"name" : row["name"], "home" : row["house"]})
                with open(s.argv[2], 'w') as file :
                    writer = csv.DictWriter(file, fieldnames = ["first", "last" , "house"])
                    writer.writeheader()
                    for i in line :
                        last, first = i["name"].split(",")
                        first = first.replace(" ","")
                        writer.writerow({"first":first , "last" : last , "house" :i["home"]})
        elif len(s.argv) > 3 :
            s.exit("Too many command-line arguments")
except FileNotFoundError :
       s.exit("Could not read "+ s.argv[1])
