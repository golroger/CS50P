import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search("(.+)\"(.+)\"(.+)$",s)
    if match :
        code = match.group(2)
        match_code = re.search("^(.+)embed/(.+)$",code)
        if match_code :
            code_2 = match_code.group(2)
            return "https://youtu.be/"+code_2
        else :
            return None
    else :
        return None


if __name__ == "__main__":
    main()