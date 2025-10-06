import math

def perfectNumber(n):
    sum = 1
    for i in range(2, math.ceil(n/2)+1):
        if n%i == 0:
            sum += i
    #print(sum)
    print(sum == n)

cont = 'Y'
while (cont == 'Y'):
    n = int(input())
    perfectNumber(n)

    cont = input()
