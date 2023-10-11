sum = 0
m = 1
for n in range(0, 21, 1):
    if m % 2 != 0:
        sum = sum + n
    m = m + 2
print(sum)
