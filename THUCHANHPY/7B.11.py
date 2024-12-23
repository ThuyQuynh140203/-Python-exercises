def is_perfect_num(n):
    if n <= 1:
        return False
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

num = int(input("Nhap so nguyen n: "))
if is_perfect_num(num):
    print(f"{num} la so hoan hao")
else:
    print(f"{num} khong phai la so hoan hao")