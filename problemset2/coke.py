a = int(50)
while a > 0:
    print(f"Amount due: {a}")
    c = int(input("Insert coin: "))
    if c == 25:
        a = a - 25
    elif c == 10:
        a = a - 10
    elif c == 5:
        a = a - 5
    else:
        a = a

print(f"Amount due: {a}")

 



#What I tried before and where we are atm
# if c == 25:
# a = a - 25
# elif c == 10:
# a = a - 10
# elif c == 5:
# a = a - 5
# else:
# c = int(input("Insert coin: "))
# print(f"Amount due: {a}")