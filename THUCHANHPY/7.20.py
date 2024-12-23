# Bài 7.20 Insertion sort

def insertion_sort(lst):
    n = len(lst)

    for i in range (1, n):
        # Lay phan tu hien tai de chen vao vi tri dung
        key = lst[i]
        j = i - 1
        # Dich chuyen cac phan tu > i len mot vi tri

        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

lst = [64, 25, 12, 22, 11]
print("Danh sách sau khi sắp xếp:", insertion_sort(lst))