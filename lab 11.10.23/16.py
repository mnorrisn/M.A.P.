import math

a = int(input())
b = int(input())
c = int(input())
delta = b * b - 4 * a * c
print(delta)
if delta < 0:
    print("Ecuatia nu are solutie")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(x1)
    print(x2)
