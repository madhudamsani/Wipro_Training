from OOP_Concepts.student import Student
from OOP_Concepts.studentgrade import Studentgrade

cc=int(input('C code: '))
cn=input('C name: ')
ci=input('City: ')
rno=int(input('R no: '))
sn=input('S name: ')
m1=int(input("M1: "))
m2=int(input("M2: "))
m3=int(input("M3: "))

#project = Student(cc, cn, ci, rno,sn, m1, m2, m3)
project = Studentgrade(cc, cn, ci, rno,sn, m1, m2, m3)
project.welcome_msg()
project.display_college_details()
print(f'Roll No: {project.rollno} \t Name: {project.stuname}'
      f'Total: {project.calculate_total()} \n Average: {project.calculate_average()}')
project.calculate_grade()
print(f'Result: {project.result}\t Grade:{project.grade}')
