# school_system.py

# Base class representing a person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.address = None

# Class representing a student, inherits from Person
class Student(Person):
    def __init__(self, std_id, name, age, grade):
        super().__init__(name, age)
        self.std_id = std_id
        self.grade = grade

    # Method to display student information
    def display_student_info(self):
        print('Student Information')
        print('-------------------')
        print(f'Student ID : {self.std_id}')
        print(f'Student Name : {self.name}')
        print(f'Student Age : {self.age}')
        if self.address:
            print(f'Student Address : {self.address}')
        print(f'Student Grade : {self.grade}')

# Class representing a teacher, inherits from Person
class Teacher(Person):
    def __init__(self, tea_id, name, age, subject):
        super().__init__(name, age)
        self.tea_id = tea_id
        self.subject = subject

    # Method to display teacher information
    def display_teacher_info(self):
        print('Teacher Information')
        print('-------------------')
        print(f'Teacher ID : {self.tea_id}')
        print(f'Teacher Name : {self.name}')
        print(f'Teacher Age : {self.age}')
        if self.address:
            print(f'Teacher Address : {self.address}')
        print(f'Teacher Subject : {self.subject}')

# Class representing a classroom
class Classroom:
    def __init__(self, teacher):
        self.teacher = teacher
        self._students = []

    # Method to add a student to the classroom
    def add_student(self, students):
        self._students.append(students)

    # Method to display classroom information
    def display_classroom_info(self):
        print('Teacher And Subject Information')
        print('-------------------------------')
        print(f'Teacher Name : {self.teacher.name}')
        print(f'Class Subject : {self.teacher.subject}')
        print()

        for student in self._students:
            student.display_student_info()

# Class representing a school
class School:
    def __init__(self):
        self._classrooms = []

    # Method to add a classroom to the school
    def add_classroom(self, classroom):
        self._classrooms.append(classroom)

    # Method to display school data
    def display_school_data(self):
        print('School Data')
        print('-----------')

        for classroom in self._classrooms:
            classroom.display_classroom_info()
