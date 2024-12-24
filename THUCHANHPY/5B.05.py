from datetime import datetime


def cal_age(birth_year):
    current_year = datetime.now().year
    return current_year - birth_year


birth_year = int(input("Nhap nam sinh: "))

if birth_year > 1900 and birth_year < datetime.now().year:
    print(cal_age(birth_year))
else:
    print("Năm sinh phải lớn hơn 1900 và nhỏ hơn năm hiện tại.")
