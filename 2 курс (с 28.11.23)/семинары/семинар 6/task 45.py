#  В ДИАПАОНЕ ОТ 0 ДО К НАЙТИ ВСЕ ДРУЖЕСТВЕННЫЕ ЧИСЛА


def div_sum(number):
    sum_divs = 1
    for div in range(2, int(number**0.5)):
        if number % div == 0:
            sum_divs += div + number // div
    return sum_divs

size= int(input("enter size of range: "))

for num_1 in range(2, size):
    num_2 = div_sum(num_1)
    if div_sum(num_2) == num_1 and num_1<num_2:
        print(num_1, num_2)
            