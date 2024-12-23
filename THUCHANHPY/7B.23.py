def is_cccd(cccd):
    cccd = str(cccd)
    if len(cccd) != 12 or not cccd.isdigit():
        return False

    province_code = int(cccd[:3])  # 3 chữ số đầu tiên là mã tỉnh
    gender_code = int(cccd[3])     # Chữ số thứ 4 là mã giới tính
    birth_code = int(cccd[4:6])    # Chữ số thứ 5 và 6 là mã năm sinh

    # Kiểm tra mã tỉnh
    if province_code < 1 or province_code > 96:
        return False

    # Kiểm tra mã giới tính và tính thế kỷ
    if gender_code % 2 == 0:  # Nam
        century = 20 + gender_code // 2
    else:  # Nữ
        century = 20 + gender_code // 2

    # Tính năm sinh đầy đủ
    full_birth_year = century * 100 + birth_code

    # Kiểm tra năm sinh hợp lệ (từ 1900 đến 2399)
    if full_birth_year < 1900 or full_birth_year > 2399:
        return False

    return True

# Ví dụ sử dụng
cccd_1 = "001203123456"  # Hợp lệ
cccd_2 = "999301234567"  # Không hợp lệ (mã tỉnh không hợp lệ)
cccd_3 = "079100123456"  # Hợp lệ
cccd_4 = "001502654321"  # Hợp lệ (Năm sinh đúng 1950)

print(is_cccd(cccd_1))  # True
print(is_cccd(cccd_2))  # False
print(is_cccd(cccd_3))  # True
print(is_cccd(cccd_4))  # True
