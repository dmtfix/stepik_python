"""При регистрации на сайтах требуется вводить пароль дважды.
 Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля.

Напишите программу, которая сравнивает пароль и его подтверждение.
Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят»."""

Pass1 = input()
Pass2 = input()
if Pass1 == Pass2:
    print("Пароль принят")
else:
    print("Пароль не принят")

"""Напишите программу, которая определяет, является число четным или нечетным."""

num = int(input())
if num % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

"""Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется
 следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр."""

number = int(input())
unit = number % 10
ten = ((number % 1000) % 100) // 10
hundred = (number % 1000) // 100
thousand = number // 1000

summa = unit + thousand
difference = hundred - ten

if summa == difference:
    print("ДА")
else:
    print("НЕТ")

"""Напишите программу, которая определяет, разрешен пользователю доступ к интернет-ресурсу или нет.
Программа должна вывести текст «Доступ разрешен» если возраст не менее 18, и «Доступ запрещен» в противном случае.
"""
age = int(input())
if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

"""Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке)
 последовательными членами арифметической прогрессии."""

num1 = int(input())
num2 = int(input())
num3 = int(input())
diff1 = num2 - num1  # В арифметической прогресии каждое последующее число больше на один и тот же шаг
diff2 = num3 - num2
if diff1 == diff2:
    print("YES")
else:
    print("NO")
"""Напишите программу, которая определяет наименьшее из двух чисел."""

num1 = int(input())
num2 = int(input())
if num1 < num2:
    print(num1)
else:
    print(num2)

"""Напишите программу, которая определяет наименьшее из четырёх чисел."""
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

a, b = 0, 0
if num1 < num2:
    a = num1
else:
    a = num2
if num3 < num4:
    b = num3
else:
    b = num4
if a < b:
    print(a)
else:
    print(b)

"""Напишите программу, которая по введённому возрасту пользователя сообщает,
 к какой возрастной группе он относится:

до 13 включительно – детство;
от 14 до 24 – молодость;
от 25 до 59 – зрелость;
от 60 – старость."""

age = int(input())
if age <= 13:
    print("детство")
if 14 <= age <= 24:
    print("молодость")
if 25 <= age <= 59:
    print("зрелость")
if age >= 60:
    print("старость")

"""Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел."""

num1 = int(input())
num2 = int(input())
num3 = int(input())

a, b, c = 0, 0, 0
if num1 > 0:
    a = num1
else:
    a = 0
if num2 > 0:
    b = num2
else:
    b = 0
if num3 > 0:
    c = num3
else:
    c = 0
print(a + b + c)
