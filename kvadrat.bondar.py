#import math

from math import sqrt as imbsqrt

bad_data = True
while bad_data == True:
    try:
        a = int(input("Введите а:"))
        b = int(input("Введите b:"))
        c = int(input("Введите c:"))
        bad_data = False
    except:
        print('Вы ввели не число')

D = b * b - (4 * a * c)
print(f'Дискриминант равен {D}')

if D < 0:
    print ('нет корней')
elif D == 0:
    x1 = (-b)/(2*a)
    print(f'один корень, x1={x1}')
elif D > 0:
    s = ibmsqrt(D)
    x1 = (-b+s)/(2*a)
    x2 = (-b-s)/(2*a)
    print(f'два корня, x1={x1}, x2={x2}')
