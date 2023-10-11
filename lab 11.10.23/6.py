prim = True
n = int(input())
for i in range(2, n, 1):
    if n % 2 == 0:
        prim = False
if prim:
    print("numarul este prim")
else:
    print("numarul nu este prim")
