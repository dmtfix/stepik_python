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