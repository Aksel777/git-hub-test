#Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
 
# list_1 = [1, 2, 3, 4, 5]
# k = 3

# # Введите ваше решение ниже
# count = 0

# for i in list_1:
#     if i == k:
#         count += 1
    
# print(count)





#Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
#Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

# list_1 = [1, 2, 3, 4, 5]
# k = 6
# min_diff = float('inf') #// функция на самое большую бесконечость
# clos_elem  = 0

# for i in list_1:
#     if k == i:
#         print(i)
    
#     difference = abs(i-k)
    
#     if difference < min_diff:
#         min_diff = difference
#         clos_elem = i
        
# print(clos_elem)





# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# Напишите программу, которая вычисляет стоимость введенного пользователем
# слова k и выводит его. Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

# new_list = str(input('enter word in Rus or Eng'))

# text = 'ноутбук'

# new_dicts = {1: 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ',
# 3:'BCMPБГЁЬЯ', 4: 'FHVWYЙЫ', 5: 'KЖЗХЦЧ', 
# 8: 'JXШЭЮ', 10: 'QZФЩЪ'}
    
# count = 0

# if text[0].upper() in new_dicts:
#     for key, value in new_dicts.items():
#         count+= key
    



# # if word[0].lower() in eng:
# #     summa = 0
# #     for letter in word:
# #         for key, value in list_English.items():
# #             if letter.upper() in value:
# #                 summa += key
#     print(f'стоимость слова = {count}')

# # Введите ваше решение ниже

# # dict = {"AEIOULNSTRАВЕИНОРСТ":1, "DGДКЛМПУ":2,"BCMPБГЁЬЯ":3,"FHVWYЙЫ":4,"KЖЗХЦЧ":5,"JXШЭЮ":8,"QZФЩЪ":10}
# # print(sum([k for i in k]))
        
# # import re
# # def isCyrillic(text):
# # 	return bool(re.search('[а-яА-Я]', text))
# # points_en = {1:'AEIOULNSTR',
# #       	2:'DG',
# #       	3:'BCMP',
# #       	4:'FHVWY',
# #       	5:'K',
# #       	8:'JZ',
# #       	10:'QZ'}
# # points_ru = {1:'АВЕИНОРСТ',
# #       	2:'ДКЛМПУ',
# #       	3:'БГЁЬЯ',
# #       	4:'ЙЫ',
# #       	5:'ЖЗХЦЧ',
# #       	8:'ШЭЮ',
# #       	10:'ФЩЪ'}
# # text = 'ноутбук'
# # if isCyrillic(text):
# # 	print(sum([k for i in text for k, v in points_ru.items() if i in v]))
# # else:
# # 	print(sum([k for i in text for k, v in points_en.items() if i in v]))

# count = 0
# new_dicts = {1: 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ',
# 3:'BCMPБГЁЬЯ', 4: 'FHVWYЙЫ', 5: 'KЖЗХЦЧ', 
# 8: 'JXШЭЮ', 10: 'QZФЩЪ'}

# for key in new_dicts:
#     for text[0] in key[value]:
#         count += key
# print(count)