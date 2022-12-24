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
