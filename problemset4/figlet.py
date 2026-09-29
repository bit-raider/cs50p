import pyfiglet
import sys

try:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in pyfiglet.FigletFont.getFonts():
            f = pyfiglet.figlet_format(input("Input: "), font=sys.argv[2])
    else:
        sys.exit("Invalid arguments")
    print("Output: ", f)
except :
    print("Invalid use")
            
