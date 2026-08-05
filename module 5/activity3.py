class student:
    grade = 10
    def __init__(self,name,hobby):
        self.name=name
        self.hobby=hobby
student1= student("mohan","nothing")
print("student1 details")
print("name",student1.name)
print("grade",student1.grade)
print("hobby",student1.hobby)
student2= student("ram","football")
student3= student("rahul","cricket")
student4= student("raman","video game")
print("hobby of {} is {}".format(student3.name,student3.hobby))
print("hobby of {} is {} and grade is  {}".format(student2.name,student2.hobby,student2.grade))
