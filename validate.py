from tabulate import tabulate
import pandas as pd

def main() :
    lis = [[1] ,[ "1234"] ,[ "1 B 2 M"]]
    df = pd.DataFrame(lis , columns =  ["N° Try" , "Your Guess", "Result"])
    print(tabulate(df , headers = ["N° Try" , "Your Guess", "Result"]))

if __name__ == "__main__" :
    main()
