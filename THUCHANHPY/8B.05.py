def fibo_seq(b):
    fib_seq = [0, 1]
    while True:
        next_val = fib_seq[-1] + fib_seq[-2]
        if next_val > b:
            break
        fib_seq.append(next_val)
    return fib_seq

def writes_to_file(a, b):
    if 0 < a < b:
        filename = f'data{a}_{b}'
        fib_seq = fibo_seq(b)
        with open(filename, 'w') as file:
            for num in fib_seq:
                if num >= a:
                    file.write(f"{num} ")
        print(f'Cac so fibo tu {a} den {b} da duoc ghi vao {filename}')

if __name__ == '__main__':
    writes_to_file(1, 20)