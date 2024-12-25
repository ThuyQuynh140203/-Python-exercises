class Retangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return (f"Rectangle with length = {self.length} and width = {self.width}\n"
                f"Area: {self.area()}\n"
                f"Perimeter: {self.perimeter()}")

def main():
    length = float(input("Nhap chieu dài: "))
    width = float(input("Nhap chieu rong: "))

    rectangle = Retangle(length, width)

    print(rectangle)
if __name__ == '__main__':
    main()