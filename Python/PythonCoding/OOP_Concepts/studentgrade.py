from OOP_Concepts.student import Student
class Studentgrade(Student):
    def __init__(self, ccode, cname, ccity, rno, sn, m1, m2, m3):
        super().__init__(ccode, cname, ccity, rno, sn, m1, m2, m3)
        self.result=''
        self.grade=None

    def calculate_result(self):
        if self.mark1>40 and self.mark2>40 and self.mark3>40:
            self.result='pass'
        else:
            self.result='fail'

    def calculate_grade(self):
        self.calculate_result()
        if self.result=='pass':
            avg=super().calculate_average()
            if avg>80:
                self.grade='A'
            elif avg>=60:
                self.grade='B'
            elif avg>=40:
                self.grade='C'
            else:
                self.grade='NA'