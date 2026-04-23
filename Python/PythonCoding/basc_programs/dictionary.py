Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
dict1={1:10,2:20,3:30}
print(dict1)
{1: 10, 2: 20, 3: 30}
dict1
{1: 10, 2: 20, 3: 30}
dict1[1]
10
dict2={'a':10,'b':20,'c':30}
dict2
{'a': 10, 'b': 20, 'c': 30}
>>> dict2['a']
10
>>> stu={'rno':101,'name':'madhu','clg':'AU'}
>>> stu[clg]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    stu[clg]
NameError: name 'clg' is not defined
>>> stu['rno']
101
>>> stu['clg']
'AU'
>>> stu['clg']='Anurag'
>>> stu['clg']
'Anurag'
>>> stu['city']='hyd'
>>> stu
{'rno': 101, 'name': 'madhu', 'clg': 'Anurag', 'city': 'hyd'}
>>> stu.get('name')
'madhu'
>>> stu.keys()
dict_keys(['rno', 'name', 'clg', 'city'])
>>> stu.values()
dict_values([101, 'madhu', 'Anurag', 'hyd'])
>>> stu.pop('city')
'hyd'
>>> stu
{'rno': 101, 'name': 'madhu', 'clg': 'Anurag'}
