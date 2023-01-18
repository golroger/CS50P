import random as rd


def main():
    life = 3 ; x_list =[] ; y_list =[] ; z_list=[] ; j=0 ; score = 1
    l = get_level()
    for i in range(10) :
        x_list.append(generate_integer(l))
        y_list.append(generate_integer(l))
        z_list.append( x_list[i] + y_list[i])
    while True :
        try :
            xx = input(str(x_list[j])+" + "+str (y_list[j])+" = ")

            if int(xx) != z_list[j] :
                life = life -1
                print("EEE")
            elif j == 9 :
                print("Score :",score)
                break
            elif int(xx)  == z_list[j] :
                j=j+1
                life = 3
                score = score + 1
            if life == 0 :
                life = 3
                print(str(x_list[j])+" + "+str(y_list[j])+" = "+str(z_list[j]))
                j = j+1

        except ValueError or TypeError :
            print("EEE value")
            life = life -1
            if life == 0 :
                print(str(x_list[j])+" + "+str(y_list[j])+" = "+str(z_list[j]))
                j= j +1



def get_level() :
        l=[1,2,3]
        while True :
            try :
                level =int(input("Level :"))
                if level not in l :
                    continue
                elif level in l :
                    return level

            except ValueError or TypeError :
                pass

def generate_integer(level):

    if level == 1 :
        return rd.randint(0,9)
    elif level == 2 :
        return rd.randint(10,99)
    elif level == 3 :
         return rd.randint(100,999)
    else :
         raise Exception("ValueError")




if __name__ == "__main__":
    main()