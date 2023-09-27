# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

a = int(input('Введите число: '))
x = 0
y = 1
n = 2

while y < a:
    x, y = y, x + y
    n += 1
if y == a:
    print (n)
else:
    print ('-1')
