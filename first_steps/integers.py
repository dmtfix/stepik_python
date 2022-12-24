"""Дополнительные операции"""
# ** -- Возведение в степень
# % -- Остаток от деления
# // -- Целочисленное деление


print(2 ** 2 ** 3)  # 2 ** (2 ** 3) = 2 ** 8

print(10 // 3)  # 3 отбрасывает десятичную часть результата
print(10 // 4)  # 2 отбрасывает десятичную часть результата
print(10 // 5)  # 2 отбрасывает десятичную часть результата
print(10 // 6)  # 1 отбрасывает десятичную часть результата
print(10 // 12)  # 0 отбрасывает десятичную часть результата
print(-10 // 3)  # -4 округление в меньшую сторону

print(10 % 3)  # 1 возвращает остаток от деления двух целых чисел
print(10 % 4)  # 2 возвращает остаток от деления двух целых чисел
print(10 % 5)  # 0 возвращает остаток от деления двух целых чисел
print(10 % 6)  # 4 возвращает остаток от деления двух целых чисел
print(10 % 12)  # 10 возвращает остаток от деления двух целых чисел
print(10 % 20)  # 10 возвращает остаток от деления двух целых чисел

#  результатом деления n % m при n < m является число n. Например, 5 % 9 = 5, 3 % 13 = 3 и т.д.

"""n школьников делят kk мандаринов поровну, неделящийся остаток остается в корзине.
 Сколько целых мандаринов достанется каждому школьнику?
 Сколько целых мандаринов останется в корзине?"""

students = int(input())
mandarins = int(input())
available = mandarins // students
basket = mandarins % students
print(available)
print(basket)

"""Безумный титан Танос собрал все 6 камней бесконечности и намеревается 
уничтожить половину населения Вселенной по щелчку пальцев.
При этом если население Вселенной является нечетным числом,
то титан проявит милосердие и округлит количество выживших в большую сторону. 
Помогите Мстителям подсчитать количество выживших."""

population = int(input())
balance = population % 2
remainders = (population + balance) // 2
print(remainders)

"""В купейном вагоне имеется 99 купе с четырьмя местами для пассажиров в каждом.
Напишите программу, которая определяет номер купе, в котором находится место с заданным номером
(нумерация мест сквозная, начинается с 1)."""

place = int(input())
compartment = (place + 3) // 4
print(compartment)

"""Напишите программу, в которой рассчитывается сумма и произведение
 цифр положительного трёхзначного числа."""

number = int(input())
a = number % 10
b = (number % 100) // 10
c = number // 100
summa = a + b + c
multiplication = a * b * c
print("Сумма цифр =", summa)
print("Произведение цифр =", multiplication)

"""Дано трехзначное число abc, в котором все цифры различны.
 Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа."""

number = int(input())
c = number % 10
b = (number % 100) // 10
a = number // 100

print((a * 100) + (b * 10) + c)
print((a * 100) + (c * 10) + b)
print((b * 100) + (a * 10) + c)
print((b * 100) + (c * 10) + a)
print((c * 100) + (a * 10) + b)
print((c * 100) + (b * 10) + a)

"""Напишите программу для нахождения цифр четырёхзначного числа."""
number = int(input())
unit = number % 10
ten = ((number % 1000) % 100) // 10
hundred = (number % 1000) // 100
thousand = number // 1000

print("Цифра в позиции тысяч равна", thousand)
print("Цифра в позиции сотен равна", hundred)
print("Цифра в позиции десятков равна", ten)
print("Цифра в позиции единиц равна", unit)
