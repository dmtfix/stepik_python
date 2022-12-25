"""Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17.
 Напишите программу, определяющую, является ли введённое число красивым.
 Программа должна вывести «YES», если число является красивым, или «NO» в противном случае."""

num = int(input())

if (1000 <= num <= 9999 and num % 7 == 0) or (1000 <= num <= 9999 and num % 17 == 0):
    print("YES")
else:
    print("NO")