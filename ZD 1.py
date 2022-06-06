import math
a = float(input('введите a: '))
b = float(input('введите b: '))
c = float(input('введите с: '))
z = int(input('Число знаков после запятой: '))
d = b ** 2 - 4 * a * c
if d > 0 and a != 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print('Уравнение имеет два корня: {:3.{}f}'.format(x1, z), "и", '{:3.{}f}'.format(x2, z))
elif d > 0 and a == 0:
    print('Это не квадратное уравнение')
elif d == 0 and a != 0:
    x = (-b / (2 * a))
    print('Уравнение имеет один корень: {:3.{}f}'.format(x, z))
elif d == 0 and a == 0:
    print('Это не квадратное уравнение')
else:
    print('Уравнение не имеет корней')


