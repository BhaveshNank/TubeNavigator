import csv

with open('London_underground_data.csv') as f:
    r = f.readlines()
    for lines in r:
        # print(lines)
        g = lines.split()
        # print(g)

        acc = g
        print(acc)
    