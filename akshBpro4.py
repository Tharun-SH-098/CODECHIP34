student={
    "name":"John",
    "age":20,
    "grade":"A"
    }
print(student["name"])
print(student["age"])
print(student.get("grade"))

student["age"]=21
print(student)

student["school"]="ABC School"
print(student)

del student["grade"]
print(student)

for key in student:
    value=student[key]
    print(key,":",value)

print(len(student))

if "grade" in student:
    print("Grade is present.")
else:
    print("Grade is not present.")

keys=student.keys()
values=student.values()

print(keys)
print(values)
    
