'''#functions
def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2


#driver
num1=int(input('enter a number'))
num2=int(input('enter another number'))

res=add(num1,num2)
print('sum:',res)

res=sub(num1,num2)
print('sub:',res)

res=mul(num1,num2)
print('mul:',res)



#ARBITARY
def add(nums):
    sum=0
    for n in nums:
        sum+=n
    return sum


nums=list()
count=int(input('How many?'))

for _ in range(1, count+1):
    nums.append(int(input('No: ')))

print(add(nums))


#lambda
num1=int(input('enter a number:'))
num2=int(input('enter another number:'))

add= lambda n1, n2: n1+n2
print(add(num1,num2))
'''

numbers=[1,2,3,4,5,6]

sq= lambda nums : [i*i for i in numbers]
print(sq(numbers))

