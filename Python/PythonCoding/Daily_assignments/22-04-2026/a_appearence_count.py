s=str(input('enter a string:'))
count=0
for index, char in enumerate(s):
    if char== 'a':
        count+=1
print('count of a:',count)