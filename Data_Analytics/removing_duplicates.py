# open teh file of points, remove duplicates, then write the unique points to a new file
with open("datasets/points.txt", "r",) as readFile:
    with open("datasets/points_unique.txt", "w") as writeFile:
        lines = readFile.readlines()

        # declare an empty set
        set = set()

        for point in lines:
            if point in set: # avoid writing the point to the file
                print(f"Reject point ({point.strip()})")
            else: # add the point to the set, for refrence later
                set.add(point)
                writeFile.write(point)
