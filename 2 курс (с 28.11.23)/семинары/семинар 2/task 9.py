# Найти проиведение от 1 до N , используя  while

n = int(input('введите целое число больше 0:'))
print(n)

res = 1
# i = 1
# # while i <= n:
# #     res = res * i
# #     i += 1
# # print(res)

while n > 1:
    res *= n
    n -= 1
print (res)