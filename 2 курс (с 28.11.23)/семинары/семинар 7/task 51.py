# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты 
# имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов отличается - то False. Для пустого 
# набора объектов, функция должна возвращать True. Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.
# Ввод: 
# values = [1, 21, 101, 61] 
# if same_by(lambda x: x % 2==0, values):
# print(‘same’)
# else:
# print(‘different’)
# Вывод:
# same

# def same_by(characteristic, objects):
#     if not objects:
#         return True
#     res = list(map(characteristic, objects))
#     print(res)
#     return all(res) == any(res)
# values = [121, 21, 101, 61] 
# if same_by(lambda x: x % 2==0, values):
#     print('same')
# else:
#     print('different')


###### ВТОРОЕ РЕШЕНИЕ


# def same_by(characteristic, objects):
#     if not objects:
#         return True
#     res = set(map(characteristic, objects))
#     print(res)
#     return len(res) == 1
# values = [121, 21, 101, 61] 
# if same_by(lambda x: x % 2==0, values):
#     print('same')
# else:
#     print('different')



########## ТРЕТЬЕ РЕШЕНИЕ

# def same_by(characteristic, objects):
#     if not objects:
#         return True
#     res = list(filter(characteristic, objects))
#     print(res)
#     return res == objects or not res
# values = [121, 4, 101, 61] 
# if same_by(lambda x: x % 2==0, values):
#     print('same')
# else:
#     print('different')


# def same_by(characteristic, objects):
#     result = list(filter(characteristic,objects))
#     print(result)
#     return result == objects or not result

# values = [5, 41, 76, 11]

# if same_by(lambda x: x % 2 == 0, values):
#     print('same')
# else:
#     print('different')




