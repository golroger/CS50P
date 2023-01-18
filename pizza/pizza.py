import sys as s
from tabulate import tabulate

#print(tabulate(table, headers, tablefmt="grid"))

def main() :
    # check the number of the cmd-line arguments
    # the name of the file

    row=[]

    try :

        if  len(s.argv) <  2 :
            s.exit("Too few command-line arguments")

        # check the python extension of the file
        elif len(s.argv) == 2 :
            name = s.argv[1]
            if name[len(name)-3:len(name)] != "csv" :
                s.exit("Not a CSV file")
        # if everything is ok, let have read the file
            else :
                name = s.argv[1]
                with open(s.argv[1],'r') as file :
                    for line in file :
                        row.append(line.rstrip().split(","))
            print(tabulate(row[1:len(row)], row[0], tablefmt="grid"))
        elif len(s.argv) > 2 :
            s.exit("Too many command-line arguments")
    except FileNotFoundError :
       s.exit("File does not exist")


if __name__== "__main__" :
    main()
