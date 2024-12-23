def save_user_info():
    filename = "data_dancu.txt"

    cccd = input("Nhap ma CCCD: ")
    ho_ten = input("Nhap ho ten: ")
    tuoi = input("Nhap tuoi: ")

    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"{cccd}|{ho_ten}|{tuoi}")

    print(f"Thong tin da duoc luu vao file {filename}")

save_user_info()