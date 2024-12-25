import math


def is_prime(n):
    if n < 1:
        return False
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def write_to_file(a, b):
    if 0 < a < b:
        filename = f'data{a}_{b}'
        with open(filename, 'w') as file:
            for num in range(a, b + 1):
                if is_prime(num):
                    file.write(f'{num} ')
    print(f'Các số nguyên tố từ {a} đến {b} đã được ghi thành công vào {filename}')

if __name__ == '__main__':
    write_to_file(1, 20)
