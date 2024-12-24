# Chuong trinh kiem tra so armstrong
def check_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    sum_num = 0
    for digit in num_str:
        sum_num += int(digit) ** num_len
    return sum_num == num

print(check_armstrong(150))
print(check_armstrong(153))