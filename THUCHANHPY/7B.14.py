import string

def is_pangram(s):
    s = str(s)
    s = s.lower()

    alphabet = set(string.ascii_lowercase)

    letter_in_s = set(s)

    return alphabet.issubset(letter_in_s)
input_str = input("Nhap chuoi")
if is_pangram(input_str):
    print(f"{input_str} la chuoi pangram")
else:
    print(f"{input_str} khong phai la chuoi pangram")