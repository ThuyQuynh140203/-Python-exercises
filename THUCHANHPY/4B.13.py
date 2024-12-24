# chuong trinh kiem tra so hoan hao
def perfect_number(num):
    if num < 1:
        return False
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num

print(perfect_number(28))
print(perfect_number(14))
print(perfect_number(12))