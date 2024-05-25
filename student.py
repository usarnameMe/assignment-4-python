class Student:
    university: str = "SkillWill University"

    def __init__(self, name: str, grade: int, age: int) -> None:
        self.name: str = name
        self.grade: int = grade
        self.age: int = age

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    @property
    def is_passing(self) -> bool:
        return self.grade > 60

    def increase_grade(self, amount: int) -> None:
        self.grade += amount


student1: Student = Student(name="Gvantsa", grade=55, age=26)

print(student1)
print(student1.is_passing)

student1.increase_grade(10)
print(student1)
print(student1.is_passing)
