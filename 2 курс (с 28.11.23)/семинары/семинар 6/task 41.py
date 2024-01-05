# сколько элементов в списке, у которых соседние ближайшие числа меньше самого элемента


from random import randint

size_1 = int(input("enter size of list_1: "))
list_1 = [randint(0, 20) for _ in range(size_1)]
print(list_1)
print(type(list_1))
count = 0

for _ in range(1, size_1-1):
    if list_1[_-1] < list_1[_] and list_1[_+1] < list_1[_]:
        count = count + 1
print(count)