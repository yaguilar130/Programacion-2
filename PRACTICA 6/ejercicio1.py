import math

class AlgebraVectorial:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        return AlgebraVectorial(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return AlgebraVectorial(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def is_perpendicular(self, other):
        return self.dot(other) == 0

    def is_parallel(self, other):
        return (self.x * other.y - self.y * other.x == 0) and (self.x * other.z - self.z * other.x == 0) and (other.magnitude() != 0)

    def projection(self, other):
        scalar = self.dot(other) / other.magnitude()**2
        return AlgebraVectorial(scalar * other.x, scalar * other.y, scalar * other.z)

    def component(self, other):
        return self.dot(other) / other.magnitude()

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

if __name__ == "__main__":
    a = AlgebraVectorial(2, 5, 0)
    b = AlgebraVectorial(4, 10, 0)

    print(f"a: {a}, b: {b}")
    print(f"Perpendiculares? {a.is_perpendicular(b)}")
    print(f"Paralelos? {a.is_parallel(b)}")
    print(f"Proyección de a sobre b: {a.projection(b)}")
    print(f"Componente de a en b: {a.component(b)}")