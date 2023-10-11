unghi = False
a = int(input())
b = int(input())
c = int(input())
if a + b + c == 180:
    unghi = True
if unghi:
    print(
        "Numerele: "
        + str(a)
        + ", "
        + str(b)
        + ", "
        + str(c)
        + " pot reprezenta un triunghi"
    )
else:
    print(
        "Numerele: "
        + str(a)
        + ", "
        + str(b)
        + ", "
        + str(c)
        + " NU 30pot reprezenta un triunghi"
    )
