import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        a, b, c, d = ip.split(".")
        if 0 <= int(a) <256 and 0 <= int(b) <256 and 0 <= int(c) <256 and 0 <= int(d) <256:
            return True
        else:
            return False

    except ValueError:
        return False


if __name__ == "__main__":
    main()