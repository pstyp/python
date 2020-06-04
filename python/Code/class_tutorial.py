class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

Jane=Student('Jane', 29)
Josh=Student('Josh', 21)

print(getattr(Jane, "age"))