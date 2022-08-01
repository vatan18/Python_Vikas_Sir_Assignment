#this is correct actually
import csv
import json

marksheet = '''
{
"exams":
[
{
  "name" : "Ram","marks1" : 10,"marks2" : 20
},
{
  "name" : "Shyam","marks1" : 45,"marks2" : 54
}
],
"status": ["ok"]
}
'''

marksheet = json.loads(marksheet)['exams']
#to find min max name_wise ie-(using row iteration)
with open("marksheet.csv", 'r') as f:  
 student=csv.reader(f)
 for row in student:
        name=row[0]
        marks=row[1:]
        print(f"student={name},max={max(marks)},min={min(marks)},")
with open("marksheet.csv", 'w') as f: 
    wr = csv.DictWriter(f, fieldnames = marksheet[0]) 
    wr.writeheader() 
    wr.writerows(marksheet)