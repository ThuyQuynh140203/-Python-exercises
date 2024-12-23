from unicodedata import normalize


def chuan_hoa(ho_ten):
    ho_ten = str(ho_ten)

    # loai bo khoang trang giua 2 dau chuoi
    ho_ten = ho_ten.strip()

    # tach chuoi ten phan biet theo khoang trang
    ho_ten = ho_ten.split()

    # Khoi tạo mang để chứa các chuỗi tên đã chuẩn hóa
    list_normalizes = []

    for ten in ho_ten:
        # Viet hoa chu cai dau của ten
        ten = ten.capitalize()
        list_normalizes.append(ten)

    normalize_name = " ".join(list_normalizes)
    return normalize_name

print(chuan_hoa("nguyễn  văN  hẬu "))

