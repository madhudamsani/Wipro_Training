'''
num1=int(input('enter a value:'))
num2=int(input('enter another value:'))
if num1==num2:
    print("both numbers are equal")
elif num1>num2:
    print(num1," is big")
else:
    print(num2, " is big")
'''

#big3
num1= int(input('enter a number'))
num2= int(input('enter another number'))
num3= int(input('enter another number'))

if num1==num2 and num2==num3:
    print('all values are equal')
elif num1>num2 and num1>num3:
    print(num1,' is greater')
elif num2>num1 and num2>num3:
    print(num2,' is greater')
else:
    print(num3,' is greater')
