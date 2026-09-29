import pyfiglet
import sys
f = str
try:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
    f = pyfiglet.figlet_format(input("Input: "), font=sys.argv[2])
    print("Output: ", f)
except:
    ...
    