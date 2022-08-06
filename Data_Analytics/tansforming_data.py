# open baby_names.csv and a new file transfomred_names.csv

with open("datasets/baby_names.csv", "r",) as readFile:
    with open("datasets/transfomred_names.txt", "w") as writeFile:
        lines = readFile.readlines()
# write only the name and frequency of all records to
validPositions = ["Name", "Frequency"]
for line in lines:
    if line == validPositions:
        print(line)

# transfomred_names.csv

