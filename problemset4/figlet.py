import pyfiglet
import sys

f = pyfiglet.figlet_format(input("Input: "), font=sys.argv[1])
print("Output: ", f)
