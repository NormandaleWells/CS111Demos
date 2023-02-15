'''
numbers = { "one":1, "two":2, "three":3, "four": 4, "five":5 }
#print(numbers[2])

print("two")
'''

class Student:

    def __init__(self, student_id, first_name, last_name):
        self.id = student_id
        self.fn = first_name
        self.ln = last_name
        self.classes = []
    
    def get_name(self):
        return f"{self.fn} {self.ln}"

    def get_id(self):
        return self.id

    def add_class(self, dept, course_number):
        new_class = (dept, course_number)
        self.classes.append(new_class)

s1 = Student(100, "Charlie", "Brown")
print(s1.get_name(), s1.get_id())
s1.add_class("CS", 111)
s1.add_class("Math", 120)
print(s1.classes)
