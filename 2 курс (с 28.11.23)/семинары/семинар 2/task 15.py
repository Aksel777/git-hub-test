#Задать количество чисел (N). Каждое в новой строчке
#найти макс и мин числа
import random

n = int(input('enter count of numbers: '))

# 1 variant

max_num = 0
min_num = 1000

for _ in range(n):
    num = random.randint(1, 50)
    print(num, end=" ")
    if num > max_num:
        max_num = num
        
    if num < min_num:
        min_num = num
        
print()        
print(max_num, min_num)


# 2 variant

max_num = 0
min_num = 1000

for _ in range(n):
    num = random.randint(1, 50)
    print(num, end=" ")
    max_num = max(max_num, num)
    min_num = min(min_num, num)
     
print()        
print(max_num, min_num)


#3 variant

num = random.randint(1, 50)
max_num = num
min_num = num

for _ in range(n - 1):
    num = random.randint(1, 50)
    print(num, end=" ")
    max_num = max(max_num, num)
    min_num = min(min_num, num)
     
print()        
print(max_num, min_num)