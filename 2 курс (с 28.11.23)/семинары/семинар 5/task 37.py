# Задача №37. Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

from random import randint

n = int(input('enter num of digit'))

def reverse_num(n):
    if n == 0:
        return " "
    k = int(input('enter digit'))
    return f'{reverse_num(n-1)} {k}'

print(reverse_num(n))
    