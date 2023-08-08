import pyfiglet
import sys
import random

fonts = pyfiglet.FigletFont.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            word = input("Input: ")
            print("Output:")
            pyfiglet.print_figlet(word, sys.argv[2])
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

elif len(sys.argv) == 1:
    word = input("Input: ")
    print("Output:")
    pyfiglet.print_figlet(word, random.choice(fonts))
    
else:
    sys.exit("Invalid usage")