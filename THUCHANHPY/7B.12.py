def is_palindrome(s):
    str = ''
    for char in s:
        if char.isalnum():
            str += char.lower()

    return str == str[::-1]

input_str = input("Nhap chuoi: ")
if is_palindrome(input_str):
    print(f"{input_str} la chuoi plindrome")
else:
    print(f"{input_str} la khong phai chuoi plindrome")