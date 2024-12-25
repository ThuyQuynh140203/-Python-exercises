import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Hàm tịnh tiến điểm với giá trị x, y được truyền vào
    def tinh_tien(self, x, y):
        self.x += x
        self.y += y

    # Khoảng cách từ điểm đến diểm o
    def khoang_cach_o(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # Khoảng cách giũa 2 điểm
    def khoang_cach(self, p_other):
        return math.sqrt((self.x - p_other.x) ** 2 + (self.y - p_other.y) ** 2)

    def __str__(self):
        return (
            f'Khoảng cách đến điểm O: {self.khoang_cach_o()}\n')


if __name__ == '__main__':
    diem1 = Point(1, 3)
    diem2 = Point(2, 4)

    print(diem1)

    diem1.tinh_tien(1, 6)
    print(f'Sau khi tinh tien: {diem1}')

    # Khoảng cách giữa hai điểm
    print(f'Khoảng cách giữa hai điểm: {diem1.khoang_cach(diem2)}')
