import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        return (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a)

    def chuvi(self):
        if not self.is_triangle():
            return "Khong phai tam giac hop le"
        return self.a + self.b + self.c

    def dientich(self):
        p = self.chuvi() / 2 #Nửa chu vi
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def lapphuong(self):
        canh = sorted([self.a, self.b, self.c])
        return math.isclose(canh[0] ** 2 + canh[1] ** 2, canh[2] ** 2)
    def loai_tam_giac(self):
        if (self.a == self.b == self.c):
            return 'Tam giác đều'
        elif (self.a == self.b or self.a == self.c or self.b == self.c) and (self.lapphuong()):
            return 'Tam giác vuông cân'
        elif (self.lapphuong()):
            return 'Tam giác vuông'
        elif (self.a == self.b or self.a == self.c or self.b == self.c):
            return 'Tam giác cân'
        else:
            return 'Tam giác thường'
    def __str__(self):
        return (f'Chu vi tam giác: {self.chuvi()}\n'
                f'Dien tích tam giac: {self.dientich()}\n'
                f'Loai tam giac: {self.loai_tam_giac()}')

if __name__ == '__main__':

    tam_giac = Triangle(6, 4, 5)
    print(tam_giac)