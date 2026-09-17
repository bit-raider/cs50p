x = str(input("CamelCase: "))

for i in x:
    if i.isupper():
        i = i.replace(i, '_%s', i)

print("Snake_case: ", i)
