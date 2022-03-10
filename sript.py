#import json
#file = open('students.json')

#data = json.load(file)

#for student in data['Students']:
#    print(f"{student['FirstName']} {student['LastName']}")


#Atrodi vidējo studentu vecumu (Age)

import json

file = open("students.json")
data = json.load(file)
print(data)

for student in data["Students"]:
    print(f"{student['FirstName']} {student['LastName']}")

#KOMANDAS UZDEVUMS 1
#Atrodi vidējo studentu vecumu (Age)

count = 0
total_age = 0
for student in data["Students"]:
    total_age += int(student["Age"])
    count += 1
print(f"Average age: {total_age/count}")