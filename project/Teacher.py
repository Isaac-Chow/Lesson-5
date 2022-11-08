# Once we've modularized a folder Python requires us to explicitly 
# state the path.
from project import Student

class Teacher:
    def __init__(self, prefix, first_name, last_name, subject, height, weight__fat):
        self.prefix=prefix
        self.fname=first_name
        self.lname=last_name
        self.subject=subject
        self.height=height
        self.weight__fat=weight__fat

    def __str__(self):
        return f"{self.prefix} {self.fname} {self.lname}(Teacher, {self.subject}\nHeight:{self.height} Weight(if>150kg=FAT):{self.weight__fat})"

    def teach(self):
        return f"Hello class! today we will learn about {self.subject}"

    def assign(self, student: Student):
        if type(student) != Student:
            pass

