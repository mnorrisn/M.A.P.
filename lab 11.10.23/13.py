sum = 0
n = int(input())
for i in range(n):
    m = int(input())
    sum = sum + m
print("Suma a celor " + str(n) + " numere este: " + str(sum))
print("Media sumei este: " + str(int(sum / n)))
