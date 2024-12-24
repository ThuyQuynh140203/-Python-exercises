# Chuong trinh may tinh thu nhỏ
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
ch = input("Nhap lua chon (+, -, *, /): ")

# Thực hiện phép toán tương ứng
if ch == "+":
    print(f"Kết quả: {a + b}")
elif ch == "-":
    print(f"Kết quả: {a - b}")
elif ch == "*":
    print(f"Kết quả: {a * b}")
elif ch == "/":
    if b == 0:
        print("Lỗi: Không thể chia cho 0.")
    else:
        print(f"Kết quả: {a / b}")
else:
    print("Ký tự ch không phải là một toán tử.")