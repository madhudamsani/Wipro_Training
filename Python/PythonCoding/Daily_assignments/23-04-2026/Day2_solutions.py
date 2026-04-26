#1st solution
#creating a list with fruits
fruits=['Apple', 'Banana', 'Orange', 'Grapes', 'Papaya']

print(fruits)

#Adding 2 more fruits
fruits.append('Guava')
fruits.append('Pineapple')

fruits.remove('Papaya')    #removing a fruit
print(fruits)

#Accessing 2nd and 4th elements
print(fruits[1])
print(fruits[3])

print(fruits[0:3])   #slice operation

print('Lenght of list:',len(fruits))   #length of list




#2nd solution
#tuple with cities
cities= ('New York', 'London', 'Delhi')
print(cities)

#print 1st and last elements of tuple
print(cities[0])
print(cities[-1])

cities1=('Hyderabad', 'Bangalore') #2nd tuple

combined_cities=cities+cities1    #concatinating two tuples
print(combined_cities)

#combined_cities[1]='Mumbai' shows error as tuple is immutable
#print(combined_cities)

#unpacking the elements of tuple and printing
city1, city2, city3= cities

print(city1)
print(city2)
print(city3)




#3rd solution
#set with colors
colors={'red', 'blue', 'green', 'yellow', 'orange'}
print('Colors: ',colors)

#add new color
colors.add('white')

#remove a color
colors.remove('yellow')
print('updated set:',colors)

#Another set with colors
colors2={'violet', 'pink', 'brown'}
print('Another set:',colors2)

#Intersection
intersection= colors.intersection(colors2)

#union
union= colors.union(colors2)

#difference
difference = colors.difference(colors2)

print('Intersection: ',intersection)
print('Union: ',union)
print('Difference: ',difference)

#check if specific color is in the set
check_color='green'
print(check_color,' is in colors set?', check_color in colors)

#convert list of fruits into set to remove duplicates
fruits = ['apple','banana', 'apple', 'orange', 'grape', 'banana']
unique_fruits=set(fruits)
print('\n Unique fruits: ',unique_fruits)




#4th solution
#create a dictionary
details = { 'name': 'Madhu',
            'age': 23,
            'favourite_hobby': 'watching movies'}
print('My details: ', details)

#print value associated with name
print('Name: ',details['name'])

#add new element
details['favourite_food']='Biryani'

#update favourite hobby
details['favourite_hobby']='listening music'

print('Updated dictionary:',details)

#print all keys and values seperately
print('\nKeys: ',details.keys())
print('\nValues: ',details.values())

#remove age element
details.pop('age')
print('\nDictionary after removing age: ',details)

