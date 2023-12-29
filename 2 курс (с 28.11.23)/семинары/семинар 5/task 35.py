# Задача №35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)


# Input: 5

# Output: yes




# n = int(input('enter digit: '))
# # def prime_num(n):
# #     for dif in range(2, n):
# #         if n%dif==0:
# #             return False
# #     return True
# # print(prime_num(n))


# # второй вариант

# def prime_num(n):
#     if n != 2 and n % 2 == 0:
#         return False
#     for div in range(3, int(n**0.5)+1, 2):
#         if n % div == 0:
#             return False
#     return True
# print(prime_num(n))
        