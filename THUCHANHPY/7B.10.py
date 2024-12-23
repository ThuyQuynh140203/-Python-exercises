import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Nhap 1 so nguyen to: "));

if is_prime(num):
    print(f"{num} la so nguyen to.")
else:
    print(f"{num} khong phai la so nguyen to")