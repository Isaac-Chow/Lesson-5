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

teach1=Teacher("Mr.", "Michael \"Fishball\"", "Ivan Yuen", "Gs, science", 183, "6969Kg")
teach2=Teacher("Miss.", "Teresa", "Chan", "Gs, Math", 150, "70Kg")
teach3=Teacher("Mr.", "Alan", "Ng", "Gs, EleGs2, Math, Cs", 150, "70Kg")
teach4=Teacher("Mr.", "Kalvin", "Chan", "Gs, Math, Cs, PE, VA, EleChi, EleGs", 150, "70Kg")
class Student:
    pass

class Visitor:
    pass

class ClassRoom:
    pass

teachers = [ teach1, teach2, teach3, teach4]
for item in teachers:
    print(item)
    print("\n")