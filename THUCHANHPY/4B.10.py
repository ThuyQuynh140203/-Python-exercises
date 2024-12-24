def convert_base(number, from_base, to_base):
    # Chuyen so nhap vào thành kiểu thập phân
    decimal_number = int(number, from_base)

    # Chuyen cơ so thap phan sang các cơ số khác
    if to_base == 2:
        return bin(decimal_number)[2:]
    elif to_base == 8:
        return oct(decimal_number)[2:]
    elif to_base == 16:
        return hex(decimal_number)[2:].upper()
    else:
        return str(decimal_number)

# Input: number, from_base, to_base
x = input("Enter the number to be converted: ")
y = int(input("Enter the base of the number (2, 8, 10, 16): "))
z = int(input("Enter the target base (2, 8, 10, 16): "))

converted_number = convert_base(x, y, z)
print(f"The number {x} in base {y} is {converted_number} in base {z}.")
