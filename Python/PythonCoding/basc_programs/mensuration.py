from mypackage.basicshapes import areaofsquare, perimeterofsquare, areaofrectangle
from mypackage.circle import areaofcircle, perimeterofcircle

radius=int(input('Enter radius:'))
side=int(input('Enter side of square:'))
length=int(input('Enter length:'))
breadth=int(input('Enter breadth:'))

print('Area of circle',areaofcircle(radius))

print('Perimeter of circle:',perimeterofcircle(radius))

print('Area of square;', areaofsquare(side))

print('Perimeter of square:', perimeterofsquare(side))

print('Area of rectangele:', areaofrectangle(length, breadth))