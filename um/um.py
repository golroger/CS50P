# By Golroger
import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # ussing Findall function that return match pattern in a list
    # using | as "OR", and go with all patterns possible
    match = re.findall(r"^Um\W+|^um$|^um\W+|\W+um\W+|\W+um$",s)
    # returning the len of the list
    return len(match)

if __name__ == "__main__":
    main()