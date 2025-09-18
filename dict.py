student = {"name" :"john",
           "age": 20,
           "marks": 75
}

print(student)
print(student["age"])

student.update({'course':'BCA'})
print('after adding new key value:\n',student)

student.update({'name':'Alexa'})
print('after updating name:\n',student)

del student['course']
print('after deleting\n:',student)