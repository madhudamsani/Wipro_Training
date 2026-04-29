import re
'''
text=input('Enter the text:')
bpattern=input('enter the beginning pattern')
epattern=input('enter the ending pattern')
bpattern='^'+bpattern
epattern=epattern+'$'

if re.search(bpattern, text):
    print('Beginning match found')
else:
    print('No beginning match found')

if re.search(epattern, text):
    print('Ending match found')
else:
    print('No match found')
'''

#digits
'''
cell=input('Enter the text:')
pat='[0-9]'

if re.search(pat , cell):
    print('only digits are present')
else:
    print('other chars present')
'''


#username
'''
user=input('Etner username:')
pat=r"[A-Z]{1,100}[a-z]{8}[0-9]"

if re.match(pat, user):
    print('Valid username')
else:
    print('Invalid username')
    

mail=input('Enter email:')
pat=r"^[a-z A-Z 0-9 _]+@[a-z]+\.[a-z]+"
if re.match(pat, mail):
    print('Email is valid')
else:
    print('Email is invalid')
'''


#password
'''
pwd=input('Enter password:')
pat=r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[-_@#]).{8,}"
if re.match(pat, pwd):
    print('Email is valid')
else:
    print('Email is invalid')
    '''

text=input("enter text:")
pat=r"\s+"
print(re.sub(pat,text, ' '))

