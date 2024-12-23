def is_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    sum_num = 0
    for digit in num_str:
        sum_num += int(digit) ** num_len
    return sum_num == n

def list_n_armstrong(n):
    armstrong_list = []
    current = 0
    while len(armstrong_list) < n:
        if is_armstrong(current):
            armstrong_list.append(current)
        current += 1
    return armstrong_list

def get_armstrong(my_list):
    armstrong_list = []
    for num in my_list:
        if is_armstrong(num):
            armstrong_list.append(num)
    return sorted(set(armstrong_list))

# def get_frequency(path_to_file):
#     with open(path_to_file, 'r') as file:  # Mở tệp văn bản
#         text = file.read()  # Đọc nội dung tệp
#     words = text.split()  # Tách nội dung tệp thành các từ
#     armstrong_counter = {}  # Khởi tạo từ điển để đếm tần suất
#     for word in words:  # Duyệt qua từng từ trong danh sách từ
#         if word.isdigit() and is_armstrong(int(word)):  # Kiểm tra xem từ có phải là số Armstrong không
#             armstrong_counter[word] = armstrong_counter.get(word, 0) + 1  # Tăng đếm tần suất
#     with open('get_frequency.log', 'w') as log_file:  # Mở tệp ghi log trong cùng thư mục với file code hiện tại
#         log_file.write(str(armstrong_counter))  # Ghi tần suất vào tệp log
#     return armstrong_counter  # Trả về từ điển tần suất
#
# # Kiểm tra hàm
# print(get_frequency('my_text_1.txt'))  # Kết quả sẽ phụ thuộc vào nội dung tệp

# e) Hàm chính để kiểm tra các câu trên
def main():
    print(is_armstrong(153))  # True
    print(list_n_armstrong(5))  # [0, 1, 2, 3, 4]
    my_list = [153, 370, 371, 407, 123, 456]
    print(get_armstrong(my_list))  # [153, 370, 371, 407]
    # print(get_frequency('my_text_1.txt'))

# Kiểm tra hàm chính
main()