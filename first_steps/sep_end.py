# sep - print('a', 'b', 'c', sep='*') ----> a*b*c (Разделитель между параметрами,
# по умолчанию пробел)
# end - print('a', 'b', 'c', end='@') ----> a b c@d (Разделитель между строками,
# по умолчанию перевод строки '\n' )

print('a', 'b', 'c', sep='*', end='finish')
print('d', 'e', 'f', sep='**', end='^__^')
print('g', 'h', 'i', sep='+', end='%')
print('j', 'k', 'l', sep='-', end='#')
print('m', 'n', 'o', sep='/', end='!')
print()
print("----------------------------")
separator = input()
string1 = input()
string2 = input()
string3 = input()

print(string1, string2, string3, sep=separator)
