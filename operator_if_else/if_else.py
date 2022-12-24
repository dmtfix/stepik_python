answer = input('Какой язык программирования мы изучаем?\n')
if answer == 'Python':
    print('Верно! Мы учим Python =)')
    print('Python - отличный язык!')
else:
    print('Не совсем так!')

# В Python существует 6 основных операторов сравнения:
# if x > 7     если x больше 7
# if x < 7     если x меньше 7
# if x >= 7    если x больше либо равен  7
# if x <= 7    если x меньше либо равен  7
# if x == 7    если x равен  7
# if x != 7    если x не равен  7

num1 = int(input())
num2 = int(input())

if num1 < num2:
    print(num1, 'меньше чем', num2)
if num1 > num2:
    print(num1, 'больше чем', num2)
if num1 == num2:  # используем двойное равенство
    print(num1, 'равно', num2)
if num1 != num2:
    print(num1, 'не равно', num2)

"""Цепочка сравнений"""
age = int(input())
if 3 <= age <= 6:
    print('Вы ребёнок')

"""Напишите программу, которая определяет, состоит ли двузначное число, введенное с клавиатуры, из одинаковых цифр.
 Если состоит, то программа выводит «ДА», в противном случае программа выводит «НЕТ»."""

num = int(input())
last_digit = num % 10  # последняя цифра числа
first_digit = num // 10  # первая цифра числа

if last_digit == first_digit:
    print('ДА')
else:
    print('НЕТ')

"""Напишите программу, которая считывает три числа и подсчитывает количество чётных чисел."""

num1, num2, num3 = int(input()), int(input()), int(input())
counter = 0  # переменная счётчик
if num1 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num2 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
print(counter)
