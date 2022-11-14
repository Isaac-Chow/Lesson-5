# Once we've modularized a folder Python requires us to explicitly 
# state the path.
from project import Teacher

class Student:
    def __init__(self,name,subject):
        self.name=name
        self.subject:list=[]
        self.subject.append(subject)

    def __str__(self):
        print(F"Name: {self.name}")
        print("Subjects:\n")
        for i in range(self.subject):
            print(i)
    
    def attendclass(self,teacher: Teacher):
        pass