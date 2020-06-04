#In a new Python file, create a class of students.

#It should contain the following attributes: name, age, and class with default value "student".

#It should also contain a method which takes in 3 test scores and prints the students average test


class Student:
    class_='student'
    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
    def score(self,score1,score2,score3):
        return (score1+score2+score3)/3


Jane = Student("Jane", "22", "student")

print(getattr(Jane, "class_"))

score1=int(input("score1= "))
score2=int(input("score2= "))
score3=int(input("score3= "))



print(Jane.score(score1,score2,score3))

