# Дано число А. определить, каким номером оно находится в Фибоначчи. 
# Если это не число фиб, вывести -1

A = int(input('введите целое положительное число > 1'))

# count = 4
# fib1 = 1
# fib2 = 1
# fib_res = fib1 + fib2

# while fib_res < A:
#     fib1 = fib2
#     fib2 = fib_res
#     fib_res = fib1 + fib2
#     count += 1

# if fib_res == A:
#     print(count)
# else:
#     print(-1)


count = 4

fib2 = 1
fib_res = 2

while fib_res < A:
    fib2, fib_res = fib_res, fib2 + fib_res
    count += 1

if fib_res == A:
    print(count)
else:
    print(-1)

