def list_fibo(n):
    # Khoi tạo danh sach voi 2 gia trị ban dau của day
    fibo_sequence = [0, 1]
    while len(fibo_sequence) < n:
        fibo_sequence.append(fibo_sequence[-1] + fibo_sequence[-2])
    return fibo_sequence[:n]

print(list_fibo(10))