student={"ram":90,
"rohan":85,
"mohan":89,
"rahul":98}
total=0
for score in student.values():
    total+=score
average = total/ len(student)
print("class average",average)