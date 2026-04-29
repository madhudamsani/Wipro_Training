from calc import Calc

calc_obj= Calc()
print(calc_obj.add(10,30))
print(calc_obj.sub(30, 20))
print(calc_obj.mul(10, 40))

numbers= [10,20,30]
size=len(numbers)
print("length:",size)

try:
    res=calc_obj.div(10, 0)
    for i in range(0, size+2):
        print(numbers[i])
except IndexError:
    print('Look at Index')
except ZeroDivisionError:
    print('O in the denominator')
else:
    print(res)
finally:
    print('Done')