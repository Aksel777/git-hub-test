###### LAMBDA + FILTER FUNCTIONS

my_list = [1, 3, 4, 7, 6, 8, 9, 5]

res_list = list(filter(lambda x: x%2 == 0, my_list))
print(res_list)
# OUT: [4, 6, 8]

my_list = [1, 3, 4, 7, 6, 8, 9, 5]

res_list = list(filter(lambda x: x*x==81, my_list))
print(res_list)

###### MAP FUNCTION

my_list = [1, 3, 4, 7, 6, 8, 9, 5]

res_list = list(map(lambda x: x%2 == 0, my_list))
print(res_list)
# OUT: [False, False, True, False, True, True, False, False]

my_list = [1, 3, 4, 7, 6, 8, 9, 5]

res_list = list(map(lambda x: x * x, my_list))
print(res_list)





my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]

numbers = input('Введите цифры через пробел').split()
print(numbers)
res_list = list(map(int , numbers))
print(res_list)
print([int(el) for el in numbers])