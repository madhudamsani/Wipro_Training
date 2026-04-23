'''1. Write a program that asks the user for their age and checks if they are eligible to
vote (18 years and older). Print a message based on their eligibility.'''

age=int(input('Enter your age:'))
if age>=18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')



'''2. Write a program that takes a year as input and checks if it is a leap year or not. 
Print the result. '''

year=int(input('Enter a year:'))

if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,' is a leap year')



'''3. Write a program that takes a number as input and checks if it is divisible by 5. 
Print a message if it is divisible or not. '''

num=int(input('Enter a number:'))

if num%5==0:
    print(num," is divisible by 5")
else:
    print(num," is not divisible by 5")



'''4. Write a program that takes a character as input and checks if it is a vowel or 
consonant. Print the result. '''

ch=input('Enter a character:')

if ch in ['a','e','i','o','u','A','E','I','O','U']:
    print(ch,' is a vowel')
else:
    print(ch, ' is a constant')



'''5. Write a program that takes a password as input and checks if it is strong (at least 
8 characters). Print a message based on the result. '''

pd=input('Enter password:')

if len(pd)>=8:
    print('password is strong')
else:
    print('password is weak and should be atleast 8 characters')



'''6. Write a program that takes a grade (A, B, C, D, F) as input and uses match-case 
to print a message corresponding to the grade (e.g., "Excellent" for A, "Good" for 
B, etc.). '''

grade=input('Enter your grade').upper()

match grade:
    case 'A':
        print('Excellent')
    case 'B':
        print('Good')
    case 'C':
        print('Average')
    case 'D':
        print('Below Average')
    case 'F':
        print('Fail')
    case _:
        print('Invalid grade')



'''7. Write a program that takes a traffic light color (Red, Yellow, Green) as input and 
uses match-case to print the corresponding action (e.g., "Stop" for Red, "Wait" 
for Yellow, etc.). '''

color=input('Enter traffic light color:').lower()

match color:
    case 'red':
        print('Stop')
    case 'yellow':
        print('Wait')
    case 'green':
        print('Go')
    case _:
        print('Invalid color')



'''8. Write a program that takes a number as input and uses a for loop to calculate its 
factorial. Print the result. '''

num=int(input('Enter a number:'))
fact=1

for i in range(1, num+1):
    fact=fact*i

print('factorial:',fact)



'''9. Write a program that uses a for loop to print all even numbers between 1 and 20. '''

print('Even numbers between 1 and 20 are:')

for i in range(1, 21):
    if i%2==0:
        print(i)



'''10. Write a program that uses a while loop to create a countdown timer from 10 to 0. 
Print each number. '''

count=10
while count >=0:
    print(count)
    count-=1



'''11. Write a program that uses a for loop to count the number of vowels in a given 
string. Print the count. '''

text=input('Enter a string:').lower()

count=0
for ch in text:
    if ch in "aeiou":
        count+=1
print(count)



'''12. Write a program that uses a for loop to print numbers from 1 to 10, but skips 
printing the number 5 (use continue) and stops the loop if the number 8 is 
reached (use break). '''

for i in range(1, 11):
    if i==5:
        continue
    if i==8:
        break
    print(i)
