def count_char(s, c):
    cnt = s.count(c)
    if cnt > 0:
        return f'Ky tu {c} xuat hien {cnt} lan trong chuoi {s}'
    else:
        return f'Ky tu {c} khong xuat hien trong chuoi {s}'

s = input("Nhap chuoi: ")
c = input("Nhap ky tu c: ")

print(count_char(s, c))