import csv

file=open("marks.csv","r")
csv_reader=csv.reader(file)
marks=[]
for row in csv_reader:
    marks[row[0]]={"name":row[1],"min":row[2],"max":row[3],"avg":row[4]}
print(marks)