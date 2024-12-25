def write_num_to_file(a, b):
    if 0 < a < b:
        filename = f"data{a}_{b}"
        with open(filename, 'w') as file:
            for num in range(a, b + 1):
                file.write(f'{num} ')
        print(f'Các số từ {a} đến {b} đã được lưu vào {filename}')
    else:
        print('Luu file that bại')

if __name__ == '__main__':
    write_num_to_file(1, 10)