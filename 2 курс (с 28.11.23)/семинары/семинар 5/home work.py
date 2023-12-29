a = 2
b = 2

def sum(a,b):
    if b == 0:
        return a
    return sum(a+1, b-1)
print(a,b)
print(sum(a, b))