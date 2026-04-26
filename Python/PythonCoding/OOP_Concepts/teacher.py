from OOP_Concepts.college import College

class Teacher(College):
    def __init__(self, ccode,cname,ccity,eid,tn,de,bp):
        self.tname=tn
        self.dept=de
        self.basicpay=bp

    def calculate_salary(self):
        return self.basicpay+ (self.basicpay * 0.2)-(self.basicpay*0.08)