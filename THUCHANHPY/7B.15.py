def convert_base(x, y, z):
    decimal_values = int(str(x), y)

    # Chuyen co so 10 sang co so 2
    if z == 2:
        return bin(decimal_values)
    elif z == 8:
        return oct(decimal_values)
    elif z == 10:
        return str(decimal_values)
    elif z == 16:
        return hex(decimal_values).upper()
    else:
        return("He so khong hop le")

x = input("Nhap co so x: ")
y = int(input("Nhap he so cua so vua nhap: "))
z = int(input("Nhap he so muon chuyen doi: "))

res = convert_base(x, y, z)

print(f"So {x} trong he so {y} chuyen sang he so {z}: ", res)