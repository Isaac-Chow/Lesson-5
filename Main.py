# Even though we've made Lesson5 a module Python only
# allows up to import from it if we were outside the folder
# Which means while inside the folder we don't need to call
# it directly 

# There appears to have been a change in Python 3.10 code
# REASON: https://peps.python.org/pep-0366/#proposed-change

# Python BUgs
# https://bugs.python.org/issue45540

# Reference Article
# https://towardsdatascience.com/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355


# This should work now
from project import Teacher

# Since the Teacher.py file also contains another import
# statement which imports the studen object, we need to further
# specify which object in the teacher class we're interested in 
billy = Teacher.Teacher("Mr.", "Billy", "Micah", "STEM",180, 80)

print(billy)


