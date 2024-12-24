a = input("Nhap ten sv: ")
b = input("Nhap msssv: ")
drl = int(input("Nhap drl: "))

if drl >= 90:
    xeploai = "Xuat sắc"
elif drl >= 80:
    xeploai = "Tốt"
elif drl >= 65:
    xeploai = "Khá"
elif drl >= 50:
    xeploai = "Trung bình"

print(xeploai)