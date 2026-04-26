from OOP_Concepts.rectangle import Rectangle
from OOP_Concepts.square import Square

sqobj= Square(34)
rectobj= Rectangle(21, 34)


print(f'Area of square: {sqobj.calculate_area()}\n Perimeter of Square: {sqobj.calculate_perimeter()}')

print(f'Area of rectangle: {rectobj.calculate_area()}\n Perimeter of rectangle: {rectobj.calculate_perimeter()}')