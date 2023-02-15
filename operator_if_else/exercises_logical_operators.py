"""Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17.
 Напишите программу, определяющую, является ли введённое число красивым.
 Программа должна вывести «YES», если число является красивым, или «NO» в противном случае."""

num = int(input())

if (1000 <= num <= 9999 and num % 7 == 0) or (1000 <= num <= 9999 and num % 17 == 0):
    print("YES")
else:
    print("NO")

"""Напишите программу, которая принимает три положительных числа и определяет,
 существует ли невырожденный треугольник с такими сторонами."""

side1 = int(input())
side2 = int(input())
side3 = int(input())

if (side1 < (side2 + side3)) and (side2 < (side1 + side3)) and (side3 < (side1 + side2)):
    print("YES")
else:
    print("NO")

"""Напишите программу, которая определяет, является ли год с данным номером високосным.
 Если год является високосным, то выведите «YES», иначе выведите «NO».

Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400."""

year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("YES")
else:
    print("NO")

"""Даны две различные клетки шахматной доски.
 Напишите программу, которая определяет, может ли ладья попасть с первой клетки на вторую одним ходом. 
 Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для
первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом ладьи можно 
попасть во вторую, или «NO» в противном случае."""

line1 = int(input())
column1 = int(input())
line2 = int(input())
column2 = int(input())

if line1 == line2 and 1 <= column2 <= 8 or column1 == column2 and 1 <= line2 <= 8:
    print("YES")
else:
    print("NO")

"""Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли король попасть 
с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. 
Программа должна вывести «YES», если из первой клетки ходом короля можно попасть во вторую,
или «NO» в противном случае."""
line1 = int(input())
column1 = int(input())
line2 = int(input())
column2 = int(input())

if line1 - 1 <= line2 <= line1 + 1 and column1 - 1 <= column2 <= column1 + 1:
    print("YES")
else:
    print("NO")

"""Даны две различные клетки шахматной доски. Напишите программу,  которая определяет,
 может ли конь попасть с первой клетки на вторую одним ходом. 
 Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для
  первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом коня можно 
  попасть во вторую или «NO» в противном случае."""

stolb1 = int(input())
strok1 = int(input())
stolb2 = int(input())
strok2 = int(input())

if stolb1 - stolb2 == 1 and (strok1 - strok2 == 2 or strok2 - strok1 == 2):
    print("YES")
elif stolb1 - stolb2 == 2 and (strok1 - strok2 == 1 or strok2 - strok1 == 1):
    print("YES")
elif stolb2 - stolb1 == 2 and (strok1 - strok2 == 1 or strok2 - strok1 == 1):
    print("YES")
elif stolb2 - stolb1 == 1 and (strok1 - strok2 == 2 or strok2 - strok1 == 2):
    print("YES")
else:
    print("NO")
