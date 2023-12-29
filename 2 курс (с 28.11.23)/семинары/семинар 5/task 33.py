# Задача №33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные 
# оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот:
# все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1

import time

from random import randint
n = int(input('введите количество оценок: '))
list_1 = [randint(1,5) for _ in range(n)]
# print(list_1)
start_1=time.time()
max_bal=max(list_1)
min_bal=min(list_1)
for i in range(len(list_1)):
    if list_1[i]==max_bal:
        list_1[i]=min_bal
end_1=time.time()
# print(list_1)
print(f'{end_1 - start_1}')



# второй вариант



max_bal=list_1[0]
min_bal=list_1[0]
start_2 = time.time()
for i in range(1, len(list_1)):
    if list_1[i]>max_bal:
        max_bal=list_1[i]
    if list_1[i]<min_bal:
        min_bal=list_1[i]
end_2 = time.time()
# print(list_1)
print(f'{end_2 - start_2}')
        
# for i in range(len(list_1)):
#     if list_1[i]==max_bal:
#         list_1[i]=min_bal        
# print(list_1)


#решебник с урока

from random import randint
import time


n = int(input('Введите количество оценок: '))
list_1 = [randint(1, 100000000) for _ in range(n)]
# print(list_1)
start_1 = time.time()
max_point = max(list_1)
min_point = min(list_1)
for i in range(len(list_1)):
    if list_1[i] == max_point:
        list_1[i] = min_point
end_1 = time.time()
# print(list_1)
print(f'{end_1 - start_1}')

# 2

start_2 = time.time()

max_point = list_1[0]
min_point = list_1[0]

for el in set(list_1):
    if el > max_point:
        max_point = el
    if el < min_point:
        min_point = el

for i in range(len(list_1)):
    if list_1[i] == max_point:
        list_1[i] = min_point

end_2 = time.time()
# print(list_1)
print(f'{end_2 - start_2}')

# 3

start_3 = time.time()

max_point = list_1[0]
min_point = list_1[0]
list_max_points = [0]

for i in range(len(list_1)):
    if list_1[i] > max_point:
        max_point = list_1[i]
        list_max_points = [i]
    elif list_1[i] == max_point:
        list_max_points.append(i)
if list_1[i] < min_point:
    min_point = list_1[i]

for i in list_max_points:
    list_1[i] = min_point

end_3 = time.time()
# print(list_1)
print(f'{end_3 - start_3}')