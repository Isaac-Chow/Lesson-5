from Lesson_5.project import Teacher

class Visitor:
    pass

class ClassRoom:
    pass

teach1=Teacher("Mr.", "Michael \"Fishball\"", "Ivan Yuen", "Gs, science", 183, "6969Kg")
teach2=Teacher("Miss.", "Teresa", "Chan", "Gs, Math", 150, "70Kg")
teach3=Teacher("Mr.", "Alan", "Ng", "Gs, EleGs2, Math, Cs", 150, "70Kg")
teach4=Teacher("Mr.", "Kalvin", "Chan", "Gs, Math, Cs, PE, VA, EleChi, EleGs", 150, "70Kg")

teachers = [ teach1, teach2, teach3, teach4]
for item in teachers:
    print(item)
    print("\n")