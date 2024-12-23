def count_words(ten):
    ten = str(ten)
    ten = ten.split()
    return len(ten)

count = count_words("Nguyen Thuy Quynh")
print(count)