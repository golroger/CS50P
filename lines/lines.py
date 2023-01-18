import sys as s

def main() :
    # check the number of the cmd-line arguments
    # the name of the file
    name = s.argv[1]



    try :

        if  len(s.argv) <  2 :
            s.exit("Too few command-line arguments")

        # check the python extension of the file
        elif len(s.argv) == 2 :
            if name[len(name)-2:len(name)] != "py" :
                s.exit("Not a Python file")
        # if everything is ok, let have read the file
            else :
                with open(s.argv[1],'r') as file :
                    lines = file.readlines()
                    print(lines_of_code(lines))
        elif len(s.argv) > 2 :
            s.exit("Too many command-line arguments")

    except FileNotFoundError :
        s.exit("File does not exist")

def lines_of_code(lines) :
    n_lines =[]
    for i in lines :
        i = i.replace(" ","") ; i=i.replace("\n","")
        n_lines.append(i)
    count = len(n_lines)

    for i in n_lines :
        if len(i) > 0 and i[0] == "#" :
            count = count - 1
        elif len(i) == 0 :
            count = count -1
    return count

if __name__== "__main__" :
    main()



