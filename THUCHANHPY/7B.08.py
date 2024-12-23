def factorial(n):
    if n < 0:
        return "Loi so nguyen khong am"
    elif n == 0 or n == 1:
        return 1
    else:
        res = 1
        for i in range (2, n + 1):
            res *= i;
        return res
n = int(input("Nhap n: "))
res = factorial(n)

print("Ket qua: ", res)