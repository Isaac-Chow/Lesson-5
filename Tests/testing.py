import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# print(PROJECT_ROOT)
sys.path.append(PROJECT_ROOT)
# print(sys.path)

from project import Teacher


teach1 = Teacher.Teacher("Mr.", "Michael \"Fishball\"", "Ivan Yuen", "Gs, science", 183, "6969Kg")
teach2 = Teacher.Teacher("Miss.", "Teresa", "Chan", "Gs, Math", 150, "70Kg")
teach3 = Teacher.Teacher("Mr.", "Alan", "Ng", "Gs, EleGs2, Math, Cs", 150, "70Kg")
teach4 = Teacher.Teacher("Mr.", "Kalvin", "Chan", "Gs, Math, Cs, PE, VA, EleChi, EleGs", 150, "70Kg")

teachers = [ teach1, teach2, teach3, teach4]
for item in teachers:
    print(item)
    print("\n")


# __package__ = sys.modules[__spec__.parent]

# print(__package__)
# print(__name__)

