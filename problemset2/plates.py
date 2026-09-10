def main():
    plate = input("Plate: ").upper()
    s = plate
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6 :
        return False
    elif not s[0:2].isalpha():
        return False
    number_started = False
    for char in s:
        if char.isdigit():
            if not number_started and char == "0":
                return False
            number_started = True
        elif number_started and char.isalpha():
            return False
        elif not char.isalnum():
            return False
    return True
        
main()

# conditions divided into categories, length done, first two chars be alphabet is done
# numbers in the middle not allowed is a problem yet to figure out
# update: done, used a killswitch and "and" is looking more interesting than I originally thought
# along with last char being only number

# and lastly no punctuation and special characters, shouldn't be that bad

#did some shit and there's a million errors, 08/09/2026, cya later
