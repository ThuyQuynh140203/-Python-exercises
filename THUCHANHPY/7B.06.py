# 7B.06
n = int(input("Nhap n: "))
def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n-1)

print(sum_recursive(n))

def sum_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_iterative(n))
