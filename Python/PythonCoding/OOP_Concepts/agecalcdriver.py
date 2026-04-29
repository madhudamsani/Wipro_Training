from OOP_Concepts.agecalc import AgeCalculation
from OOP_Concepts.myexception import AgeException

age =int(input("Age: "))
aobj=AgeCalculation()

try:
    if aobj.voting_age_check(age):
        print('Eligible. Contact next step..')
    if aobj.pension_age_check(age):
        print('Eligible for pension')

except AgeException as ae:
    print(ae)
