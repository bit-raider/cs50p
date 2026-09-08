def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) <2 or len(s) > 7 :
        return False
    elif not s[0, 1].isalpha():
        return False
    elif ... :
        ...

main()

# conditions divided into categories, length done, first two chars be alphabet is done
# numbers in the middle not allowed is a problem yet to figure out
# along with last char being only number
# and lastly no punctuation and special characters, shouldn't be that bad

