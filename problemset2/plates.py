def main():
    plate = input("Plate: ").upper()
    s = str
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if char.isdigit() or char.isalpha():
        if len(s) < 2 or len(s) > 6 :
            return False
        elif not s[0, 1].isalpha():
            return False
        number_started = False
        for char in s:
            if char.isdigit():
                number_started = True
            elif number_started and char.isalpha():
                return False
    else:
        return False
    
        
main()

# conditions divided into categories, length done, first two chars be alphabet is done
# numbers in the middle not allowed is a problem yet to figure out
# update: done, used a killswitch and "and" is looking more interesting than I originally thought
# along with last char being only number

# and lastly no punctuation and special characters, shouldn't be that bad


