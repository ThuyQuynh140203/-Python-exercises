# Chuong trinh tinh phu cap
hoten = input("Nhap ho ten nhan vien: ")
chucvu = input("Nhap chuc vu nhan vien: ")

if chucvu == "Giám đốc":
    phucap = 5000000
elif chucvu == "Phó Giám Đốc":
    phucap = 3000000
elif chucvu == "Truong Phong":
    phucap = 500000
else:
    phucap = 0

print(f"Can bo {hoten} chuc vu {chucvu} có phu cap {phucap}")