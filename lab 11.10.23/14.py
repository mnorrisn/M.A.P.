import sys

nrmare = int(-sys.maxsize)
nrmic = int(sys.maxsize)
v = []
n = int(input())
for i in range(n):
    v.append(int(input(3)))
    if v[i] > nrmare:
        nrmare = v[i]
    if v[i] < nrmic:
        nrmic = v[i]
print("Cel mai mare numar: " + str(nrmare))
print("Cel mai mic numar: " + str(nrmic))
