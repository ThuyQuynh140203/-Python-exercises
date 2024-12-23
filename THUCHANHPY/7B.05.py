#Bai 7B05
def max_value(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = float(input("Nhap so thu nhat: "))
num2 = float(input("Nhap so thu hai: "))
num3 = float(input("Nhap so thu 3: "))

res = max_value(num1, num2, num3)

print("So lon nhat trong 3 so: ", res)