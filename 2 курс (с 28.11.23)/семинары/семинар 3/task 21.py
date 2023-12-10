# Задача №21. Напишите программу для печати всех уникальных значений в словаре.

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

list_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
              {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

unique_values = set()

# for item in list_dicts:
#     for key in item:
#         unique_values.add(item[key].strip()) # стрип удалет пробелы и табуляцию
        
# print(unique_values)


# #  решeние  2

# unique_values = set()

# for item in list_dicts:
#     for key in item.keys():
#         unique_values.add(item[key].strip()) # стрип удалет пробелы и табуляцию
        
# print(unique_values)




# unique_values = set()

# for item in list_dicts:
#     for value in item.values():
#         unique_values.add(value.strip()) # стрип удалет пробелы и табуляцию
        
# print(unique_values)





# unique_values = set()

# for item in list_dicts:
    
#     unique_values.add(*item.values()) 
        
# print(unique_values)





unique_values = set()

for item in list_dicts:
    
    unique_values.update(item.values()) 
        
print(unique_values)