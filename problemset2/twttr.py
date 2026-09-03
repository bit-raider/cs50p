a = input("Input: ")
result = ""
vowel = ["a", "e", "i", "o", "u"]

for i in a:
    if i.lower() not in vowel:
        result = result + i
    else:
        result = result

print(f"Output: {result}")