def read_and_sum(filename):
    with open(filename, 'r') as file:
        content = file.read()

    str_values = content.split()

    values = []
    for val in str_values:
        values.append(int(val))

    total = 0
    for val in values:
        total += val

    with open(filename, 'a') as file:
        file.write(f'\n{total}\n')
    print(f"Tong cac gia tri duoc tinh va luu vao {filename}")

if __name__ == '__main__':
    read_and_sum('data1_10')

# def read_and_sum_values_from_file(file_name):
#     try:
#         # Đọc dữ liệu từ tệp
#         with open(file_name, 'r') as file:
#             lines = file.readlines()
#
#         values = []
#         for line in lines:
#             stripped_line = line.strip()
#             value = int(stripped_line)
#             values.append(value)
#
#         total_sum = 0
#         for value in values:
#             total_sum += value
#
#         # Mở tệp ở chế độ append để ghi thêm dữ liệu vào cuối tệp
#         with open(file_name, 'a') as file:
#             file.write(f"Tổng: {total_sum}\n")
#
#         print(f"Tổng các giá trị trong tệp {file_name} đã được tính và ghi nối vào tệp.")
#     except Exception as e:
#         print(f"Đã xảy ra lỗi khi đọc hoặc ghi tệp: {e}")
#
# # Ví dụ sử dụng hàm
# read_and_sum_values_from_file("data1_20.txt")
