v = []
for i in range(8):
    v.append(int(input()))
for i in range(8):
    print(str(v[i]) + " ", end="")
for i in range(8):
    for j in range(i, 8, 1):
        if v[i] > v[j]:
            v[i], v[j] = v[j], v[i]
            for k in range(8):
                print(str(v[k]) + " ", end="")
            print()
