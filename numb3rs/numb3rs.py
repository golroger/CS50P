import re
import sys


def main():

           ip = input("IPv4 Address: ").strip()
           print(validate(ip))

# ip adresse format # . # . # . # where # should be a number between 0 and 255

# ^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$
def validate(ip):

    if re.search(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip) :
        return True
    else :
        return False
if __name__ == "__main__":
    main()