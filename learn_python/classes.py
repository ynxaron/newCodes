class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name --> {self.name}\nAge --> {self.age}"

    def greet(self):
        return f"Hello, I am {self.name} and I am {self.age} years old"


p1 = Person("Satyam", 21);
print(p1.greet())
print(p1)

class Student(Person):
    def __init__(self, l: str, r: str, graduationYear: int, currentYear: int):
        super().__init__(l, int(r))
        self.graduationYear = graduationYear
        self.currentYear = currentYear

    def greet(self):
        primgreet = super().greet()
        return f"{primgreet} and I am a student, currently in {self.currentYear}, would graduate on {self.graduationYear}"

s1 = Student("Aryavatta", "34", 2026, 2025);
print(s1.greet())
