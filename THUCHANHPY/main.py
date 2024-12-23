#Bai 7B04
import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
def sum_prime(limit):
    total = 0
    for num in range(limit + 1):
        if is_prime(num):
            total += num
    return total

res = sum_prime(1000)
print("Tong cac so nguyen to tu 0-1000: ", res)
