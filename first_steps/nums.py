num1 = 7  # num1 - это число
num2 = 10  # num2 - это число
num3 = num1 + num2  # num3 - это число
print(num3)

s = '1992'
year = int(s)  # Преобразование строки к целому числу

num = 17
s = str(17)  # Преобразование целого числа к строке

"""Напишите программу вывода на экран трех последовательно идущих чисел, каждое на отдельной строке.
 Первое число вводит пользователь, остальные числа вычисляются в программе."""

first_num = int(input())
print(first_num)
print(first_num + 1)
print(first_num + 2)  # print(first_num,first_num + 1, first_num + 2, sep = "\n")

"""Напишите программу, вычисляющую объём куба и площадь его полной поверхности,
 по введённому значению длины ребра."""

edge = int(input())
volume = edge * edge * edge  # объём куба (a**3)
area = 6 * edge * edge  # площадь(6*(a**2))
print("Объем =", volume)
print("Площадь полной поверхности =", area)


"""Небольшая функция"""
a = int(input())
b = int(input())
function = 3 * ((a + b) ** 3) + 275 * b ** 2 - 127 * a - 41
print(function)
