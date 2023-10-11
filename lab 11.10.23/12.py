n = int(input())
v = [1, 2]
for i in range(1, n, 1):
    v.append(v[i - 1] + v[i])
for i in range(n):
    print(str(v[i]) + " ", end="")
