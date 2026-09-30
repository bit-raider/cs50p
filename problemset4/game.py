import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
        else:
            continue
    except ValueError:
        continue

num = random.randint(1,level)

while True:
    try:
        g = int(input("Guess: "))
        if g > num:
            print("Too large!")
        elif g < num:
            print("Too small!")
        elif g == num:
            print("Just right!")
            break
    except ValueError:
        continue

# tried but didn't work I think:

# while True:
#     try:
#         guess = int(input("Guess: "))
#         if guess > 0:
#             break
#         else:
#             continue
#     except ValueError:
#         continue