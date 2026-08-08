class Student:
    def _init_(self,name,marks):
        self.name=name
        self.marks=marks
    def _str_(self):
        return f"Student(Name:{self.name},Marks:{self.marks})"
s=Student("Rahul",90)
print(s)                                                              