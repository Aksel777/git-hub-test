# посчитать все повторения

from random import randint

size_1 = int(input("enter size of list_1: "))
list_1 = [randint(0, 20) for _ in range(size_1)]
print(list_1)

counter = 0

# for _ in range(size_1-1):
#     for j in range(_+1, size_1):
#         if list_1[_] ==  list_1[j]:
#             count = count + 1
# print(count)

#  ВТОРОЙ ВАРИАНТ

for _ in range(size_1-1):
    counter += list_1[_+1:].count(list_1[_])
    
print(counter)
