#print natural numbers
'''
num=int(input('Enter a number'))
val=1
while val <= num:
    print(val)
    val+=1
'''

#armstrong number
num=input('Enter a number')
val=len(num)
n=int(num)
sum=0
while(n>0):
    rem=n%10
    sum+=rem**val
    n//=10
if sum==int(num):
    print(num,' is armstrong')
else:
    print(num,' is not armstrong')
