def main() :
    w= input( "put your str :")
    x=shorten(w)
    print(x)


def shorten(word):

        v = ['e','a','o','i','u','E','O','A','I']
        txx = ""
        for i in word :
            if i not in v :
                txx = txx + i

        return txx


if __name__ == "__main__" :
    main()