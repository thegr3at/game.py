colors = {"green", "red", "red", "blue", "pink", "red", "blue,", "blue"}
numberSet = {42, 24, 7, 3, 19, 34, 13, 12}

print(colors)
print(numberSet)
print()

for color in colors:
    print(f"Color: {color}")

if 19 in numberSet:
    print("Found 19")
else:
    print("Not found")
