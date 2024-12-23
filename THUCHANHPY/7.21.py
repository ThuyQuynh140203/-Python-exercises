def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])

    return merge_lst(left_half, right_half)


def merge_lst(left, right):
    """
    Gộp hai danh sách đã được sắp xếp thành một danh sách duy nhất.

    Args:
        left (list): Danh sách bên trái đã sắp xếp.
        right (list): Danh sách bên phải đã sắp xếp.

    Returns:
        list: Danh sách đã được gộp và sắp xếp.
    """
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Thêm các phần tử còn lại
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


# Ví dụ sử dụng
lst = [64, 25, 12, 22, 11]
print("Danh sách sau khi sắp xếp (Merge Sort):", merge_sort(lst))