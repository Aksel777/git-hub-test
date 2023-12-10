# определить количество эксклюзивных чисел
from random import randint


size = int (input ('enter count of numbers: '))
# list1 = []

# for _ in range(size):
#     list1.append(randint(1,30))
    
# print(list1)

list2 = [randint(1,30) for _ in range(size)]
print(list2)

uniq = set(list2)
print(uniq)
print(len(uniq))

# print(len(set(list2))) 

    
    
    