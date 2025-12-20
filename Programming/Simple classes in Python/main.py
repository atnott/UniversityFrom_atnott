from math import *

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = int(input("Введите координату x: "))
        self.y = int(input("Введите координату y: "))

    def getLength(self):
        length = (self.x**2 + self.y**2)**0.5
        return length

    def getAngle(self):
        k = self.y / self.x
        return atan(k)

    def getSum(self, other):
        return (self.x + other.x), (self.y + other.y)

    def getSub(self, other):
        return (self.x - other.x), (self.y - other.y)

    def getScalar(self, other):
        return self.x*other.x + self.y*other.y

vector1 = Vector()
vector2 = Vector()
print(f"Длина вектора: {vector1.getLength()}")
print(f"Угол наклона: {vector1.getAngle()}")
print(f"Сумма векторов: {vector1.getSum(vector2)}")
print(f"Вычитание векторов: {vector1.getSub(vector2)}")
print(f"Скалярное произведение векторов: {vector1.getScalar(vector2)}")