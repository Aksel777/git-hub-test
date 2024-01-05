# ввести элементы первого списка, которых нет во втором, сохраняя последовательность

from random import randint
size_1 = int(input("enter size list_1: "))
list_1 = [randint(1, 30) for _ in range(size_1)]
size_2 = int(input("enter size list_2: "))
list_2 = [randint(1, 30) for _ in range(size_2)]
print(list_1)
print(list_2)

set_2 = set(list_2)                 # чтобы во втором списке повторяющиеся элементы повторно не проверялись

for _ in list_1:
    if _ not in set_2:
        print(_, end = ' ')