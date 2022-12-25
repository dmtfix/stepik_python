"""Если требуется проверить несколько условий, в языке Python используется каскадный условный оператор.
Синтаксис каскадного условного оператора имеет следующий вид:
if условие1:
    блок кода
elif условие2:
    блок кода
...
else:
    блок кода
"""

grade = int(input('Введите вашу отметку: '))

if grade >= 90:
    print(5)
elif grade >= 80:
    print(4)
elif grade >= 70:
    print(3)
elif grade >= 60:
    print(2)
else:
    print(1)

"""Даны три целых числа. Определите, сколько среди них совпадающих.
Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает)
или 0 (если все числа различны).
"""
#  1 способ. Использование вложенного условного оператора.

, b, c = int(input()), int(input()), int(input())
if a == b:
    if b == c:
        print(3)
    else:
        print(2)
else:
    if a == c:
        print(2)
    else:
        if b == c:
            print(2)
        else:
            print(0)


#  2 способ. Использование каскадного условного оператора.

a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b != c:
    print(2)
elif a != b == c:
    print(2)
elif a == c != b:
    print(2)
else:
    print(0)


#3 способ. Использование каскадного условного оператора и логического оператора or.

a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b != c or a != b == c or a == c != b:
    print(2)
else:
    print(0)