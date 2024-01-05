# Есть код:

# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#   print(‘ok’)
# else:
#   print(‘fail’)

# - В переменную transformation нужно прописать такую функцию, что бы в 
# переменной transformed_values получилась копия списка values

# решение 1

transformation = lambda x: x
values = [2, 3, 5, -7, 11, 13, 17, 19, 23, 29] 
transformed_values = list(map(transformation, values))
if values == transformed_values:
  print('ok')
else:
  print('fail')
  
  
#  решение 2 

values = [2, 3, 5, -7, 11, 13, 17, 19, 23, 29]  
transformed_values = list(values.copy())
print(transformed_values)