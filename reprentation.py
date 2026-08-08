class Student:
    def _init_(self,name,marks):
        self.name=name
        self.marks=marks
    def _str_(self):
        return f"{self.name} scored {self.marks}"
    def _repr_(self):
        return f"Student('{self.name}',{self.marks})"
s=Student("Rhaul",90)
print(s)
print(repr(s))                                                          