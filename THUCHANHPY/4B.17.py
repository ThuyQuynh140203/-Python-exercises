def check_str(s1, s2):
    # Kiểm tra chuỗi s2 có trong s1 hay không
    vitri = s1.find(s2)
    if vitri != -1:
        return f"Chuỗi '{s2}' xuất hiện lần đầu tiên trong chuỗi '{s1}' tại vị trí {vitri}."
    else:
        return f"Không tìm thấy chuỗi '{s2}' trong chuỗi '{s1}'."

s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")

res = check_str(s1, s2)
print(res)