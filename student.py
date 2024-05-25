class Student:
    university = "SkillWill University"

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    @property
    def is_passing(self):
        return self.grade > 60

    def increase_grade(self, amount):
        self.grade += amount


student1 = Student(name="Gvantsa", grade=55, age=26)

print(student1)
print(student1.is_passing)

student1.increase_grade(10)
print(student1)
print(student1.is_passing)
