import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'^.+embed/(.+)', s):
        code = matches.group(1)
        if '"' in code:
            link = "https://youtu.be/"+code.split('"')[0]
            return link
        else:
            link = "https://youtu.be/"+code
            return None

if __name__ == "__main__":
    main()