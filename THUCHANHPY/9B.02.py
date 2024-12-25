import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return (f"Circumference: {self.circumference():.2f}\n"
                f"Area: {self.area():.2f}")

def main():
    radius = float(input("Nhap ban kinh: "))

    circle = Circle(radius)

    print(circle)

if __name__ == '__main__':
    main()
