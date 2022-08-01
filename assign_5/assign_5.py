from csv import DictReader

file=DictReader(open("square.csv","r"))
for row in file:
    print(row)
