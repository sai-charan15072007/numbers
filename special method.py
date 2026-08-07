class Student:
    def __init__(self, name, marks, address):
        self.name = name
        self.marks = marks
        self.address = address
    def __str__(self):
        return f"student(name={self.name}, marks={self.marks}, address={self.address})"
s = Student("pranay",90,"hyderabad")
print(s)

class Student:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

s1 =Student("pranay")
s2 = Student("pranay")
s3 = Student("hemanth")

print(s1==s2)
print(s1==s3)


class Student:

    def __init__(self,name, roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    def __str__(self):
        return f"name: {self.name}, roll: {self.roll}, marks: {self.marks}"
    def __repr__(self):
        return f"student('{self.name}', {self.roll}, {self.marks})"
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.roll == other.roll
        return False
s1 = Student("pranay", 1, 90)
s2 = Student("prana", 1, 90)
s3 = Student("hemanth", 2, 80)

print(s1)
print(repr(s1))
print(s1==s2)
print(s1==s3)