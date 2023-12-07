# from math import ceil
# import math

# s = int(input("Enter disance:"))
# n = int(input("Enter speed:"))

# print(ceil(s/n))

# print((s+(n-1))//n)



# вторая задача

# a = int(input("enter number of pupil in 1st class"))
# b = int(input("enter number of pupil in 2nd class"))
# c = int(input("enter number of pupil in 3rd class"))
# print(math.ceil(a/2) + math.ceil(b/2) + math.ceil(c/2))
# print(((a+1)//2) + ((b+1)//2) + ((c+1)//2))



# третья задача

# i = int(input("enter number Vitja"))
# j = int (input("enter fact number"))

# if i==j:
#     print("I can not to say")
# else:
#     print ((i+j)-1)


#четвертая задача

# Year = int (input('enter number of year:'))

# if Year%4==0 and Year%100!=0:
#     print ("да, год високосный")
# elif Year%400==0:
#     print ('да, год високосный')
# else:
#     print ("нет, год обычный")



n = 16
num = 0
k = 0

while num <= n:
    num = 2 ** k
    print(num)
    k += 1