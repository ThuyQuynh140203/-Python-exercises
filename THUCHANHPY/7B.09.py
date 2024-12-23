
def count_upper_lower(s):
    upper_count = 0;
    lower_count = 0;

    for c in str(s):
        if c.isupper():
            upper_count += 1
        elif c.islower():
            lower_count += 1
    return upper_count, lower_count
s = input("Nhap chuoi: ")
print("Ket qua:", count_upper_lower(s))