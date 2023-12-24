var1 = '5 4'
var2 = '10 30 6 35 50'
var3 = '30 7 4 50'

mol = [int(x) for x in var1.split()]
n = mol[0]
m = mol[1]

set1 = set()
set2 = set()
list1 = list()
a = [int(x) for x in var2.split()]
k = set(a)
for i in k:
    set1.add(i)
b = [int(x) for x in var3.split()]
k1 = set(b)
for i in k1:
    set2.add(i)

lok = set1 & set2
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end = ' ')