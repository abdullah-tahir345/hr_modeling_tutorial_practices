# program.py

# Importing classes from the school_system and contacts modules
from school_system import Student, Teacher, Classroom, School
from contacts import Address
# Test Case 1: Creating and displaying school data
school = School()

# Creating teachers
barbie = Teacher(1, 'Barbie', 52, 'Basic Electronics')
auston = Teacher(2, 'Auston', 45, 'Databases And Management System')

# Creating students
james = Student(1, 'James', 21, 12)
melena = Student(2, 'Melena', 20, 12)
jane = Student(3, 'Jane', 22, 12)
potter = Student(4, 'Potter', 20, 12)
harry = Student(5, 'Harry', 20, 12)

# Creating addresses
address_1 = Address('11th Street', 'Lahore', 'Punjab', 55879)
address_2 = Address('09th Street', 'Islamabad', 'Punjab', 45451)
address_3 = Address('12th Street', 'Islamabad', 'Punjab', 56121)
address_4 = Address('05th Street', 'Quetta', 'Balochistan', 35413)

# Assigning addresses to students
james.address = address_1
melena.address = address_2
jane.address = address_3
potter.address = address_2  # Sharing address with Melena
harry.address = address_4

# Assigning addresses to teachers
barbie.address = Address('55th Street', 'Lahore', 'Punjab', 55549)
auston.address = Address('10th Street', 'Quetta', 'Balochistan', 35412)

# Creating classrooms
c1 = Classroom(barbie)
c2 = Classroom(auston)

# Adding students to classrooms
c1.add_student(james)
c1.add_student(melena)
c1.add_student(jane)

c2.add_student(james)
c2.add_student(potter)
c2.add_student(harry)

# Adding classrooms to school
school.add_classroom(c1)
school.add_classroom(c2)

# Displaying school data
school.display_school_data()
