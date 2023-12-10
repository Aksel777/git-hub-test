# сдвинуть последовательость из N чисел на  K элементов влево
from random import randint




list1 = [_ for _ in range(1, randint(2,20))]

print(list1)

k = int(input('enter count of shift: ')) 


# for _ in range(k):
#     last_el = list1.pop()
#     list1.insert(0, last_el)
# print(list1)
    
    
print(list1[-k:] + list1[:-k])
