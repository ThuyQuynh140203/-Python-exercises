#Bài 7.19 Selection sort

def selectionSort(list):
    n = len(list)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if (list[j] < list[min_index]):
                min_index = j

        list[i], list[min_index] = list[min_index], list[i]
    return list

list = [64, 25, 12, 22, 11]
print("Danh sach sau khi seleection sort: ", selectionSort(list))
