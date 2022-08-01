import csv

file=open("student.csv","r")
csv_reader=csv.reader(file)
student={}
for row in csv_reader:
    student[row[0]]={"age":row[1],"education":row[2],"weight":row[3]}
print(student)