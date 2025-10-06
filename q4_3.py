sum = 0
n = int(input())
min = n
while (n != 0):
    if (min > n):
        min = n
    sum += n
    n = int(input())
print("sum =",sum)
print("min =",min)